import os
import time
import random
import sqlite3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

#Importer depuis le fichier settings local
from settings import DB_PATH, LOGOS_DIR, LEAGUES, SAISON, STANDING_URL, BASE_URL

#Nombre de téléchargements simultanés
NB_WORKERS = 5

#Agent utilisateur mobile
USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Mobile Safari/537.36"
)


def recuperer_cookies_fbref() -> dict:
    #Ouvrir un vrai navigateur une seule fois pour récupérer les cookies FBref
    logger.info("Récupération des cookies FBref via Playwright...")
    cookies_dict = {}

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            args=["--no-sandbox", "--disable-blink-features=AutomationControlled"]
        )
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=USER_AGENT,
        )
        context.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        page = context.new_page()

        #Visiter FBref pour passer Cloudflare et récupérer les cookies
        page.goto("https://fbref.com/en/", wait_until="domcontentloaded", timeout=60000)
        logger.info("Attente passage Cloudflare (30s)...")
        page.wait_for_timeout(30000)

        #Extraire tous les cookies de la session
        cookies = context.cookies()
        for cookie in cookies:
            cookies_dict[cookie["name"]] = cookie["value"]

        browser.close()

    logger.success(f"✅ {len(cookies_dict)} cookies récupérés")
    return cookies_dict


def scraper_logos_depuis_page(ligue_nom: str, cookies: dict) -> dict:
    #Scraper les URLs des logos depuis la page classement FBref
    info = LEAGUES[ligue_nom]
    url = STANDING_URL.format(
        base=BASE_URL,
        lid=info["id"],
        saison=SAISON,
        slug=info["slug"],
    )

    headers = {
        "User-Agent": USER_AGENT,
        "Referer": "https://fbref.com/en/",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    logos = {}

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=30)
        bsoup = BeautifulSoup(response.text, "html.parser")

        #Chercher la table du classement
        table = None
        for t in bsoup.find_all("table"):
            tid = t.get("id", "")
            if "results" in tid and "overall" in tid:
                table = t
                break

        if table is None:
            logger.warning(f"Table introuvable pour {ligue_nom}")
            return logos

        #Extraire les logos depuis chaque ligne de la table
        for tr in table.find("tbody").find_all("tr"):
            if tr.get("class") and ("spacer" in tr.get("class") or "thead" in tr.get("class")):
                continue

            cell = tr.find(["td", "th"], {"data-stat": "team"})
            if not cell:
                continue

            equipe = cell.get_text(strip=True)
            if not equipe:
                continue

            #Chercher l'image du logo dans la cellule
            img = cell.find("img")
            if img and img.get("src"):
                logo_url = img.get("src")
                #Compléter l'URL si elle est relative
                if logo_url.startswith("/"):
                    logo_url = f"https://fbref.com{logo_url}"
                logos[equipe] = logo_url
                logger.info(f"Logo trouvé : {equipe} → {logo_url}")

        logger.success(f"{ligue_nom} : {len(logos)} logos trouvés")

    except Exception as e:
        logger.error(f"Erreur scraping logos {ligue_nom} : {e}")

    return logos


def enregistrer_logo_db(equipe: str, ligue: str, chemin: str) -> None:
    #Sauvegarder le chemin du logo dans la base de données
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS logos_clubs (
            equipe     TEXT NOT NULL,
            ligue      TEXT NOT NULL,
            chemin     TEXT,
            telecharge INTEGER DEFAULT 0,
            PRIMARY KEY (equipe, ligue)
        )
    """)
    conn.execute("""
        INSERT OR REPLACE INTO logos_clubs (equipe, ligue, chemin, telecharge)
        VALUES (?, ?, ?, 1)
    """, (equipe, ligue, chemin))
    conn.commit()
    conn.close()


def telecharger_logo(args: tuple) -> tuple[str, str, str | None]:
    #Télécharger un logo de club avec requests et les cookies FBref
    equipe, ligue, logo_url, cookies = args

    os.makedirs(LOGOS_DIR, exist_ok=True)

    nom_fichier = f"{equipe.replace(' ', '_').lower()}.png"
    chemin_local = os.path.join(LOGOS_DIR, nom_fichier)

    #Vérifier si le logo existe déjà sur le disque
    if os.path.exists(chemin_local):
        logger.info(f"Déjà présent : {nom_fichier}")
        return equipe, ligue, chemin_local

    #Pause courte pour ne pas surcharger le CDN
    time.sleep(random.uniform(0.3, 0.8))

    headers = {
        "User-Agent": USER_AGENT,
        "Referer": "https://fbref.com/en/",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
        #Header CDN nécessaire pour les logos sur cdn.ssref.net
        "Origin": "https://fbref.com",
    }

    for tentative in range(3):
        try:
            response = requests.get(
                logo_url,
                headers=headers,
                cookies=cookies,
                timeout=15
            )

            #Accepter tout contenu > 50 bytes car les mini logos sont très petits
            if response.status_code == 200 and len(response.content) > 50:
                with open(chemin_local, "wb") as f:
                    f.write(response.content)
                return equipe, ligue, chemin_local

            elif response.status_code == 404:
                #Logo inexistant sur le CDN
                return equipe, ligue, None

            else:
                logger.warning(f"Erreur {response.status_code} pour {equipe}")
                time.sleep(3)

        except Exception as e:
            logger.warning(f"Tentative {tentative + 1}/3 échouée pour {equipe} : {e}")
            time.sleep(5)

    return equipe, ligue, None


def telecharger_tous_logos() -> dict:
    #Scraper et télécharger tous les logos des clubs en parallèle
    resultats = {}

    #Récupérer les cookies via Playwright une seule fois
    cookies = recuperer_cookies_fbref()

    #Collecter tous les logos depuis toutes les ligues
    tous_logos = {}
    for ligue_nom in LEAGUES:
        logger.info(f"Scraping logos : {ligue_nom}")
        logos = scraper_logos_depuis_page(ligue_nom, cookies)
        for equipe, logo_url in logos.items():
            tous_logos[(equipe, ligue_nom)] = logo_url
        time.sleep(random.uniform(2, 4))

    total = len(tous_logos)
    logger.info(f"{total} logos à télécharger")

    if total == 0:
        logger.warning("Aucun logo trouvé — vérifie les URLs FBref")
        return resultats

    #Préparer les arguments pour chaque worker
    args_list = [
        (equipe, ligue, logo_url, cookies)
        for (equipe, ligue), logo_url in tous_logos.items()
    ]

    #Télécharger en parallèle avec les cookies
    with ThreadPoolExecutor(max_workers=NB_WORKERS) as executor:
        futures = {
            executor.submit(telecharger_logo, args): args
            for args in args_list
        }

        for i, future in enumerate(as_completed(futures), start=1):
            equipe, ligue, chemin = future.result()

            if chemin:
                resultats[(equipe, ligue)] = chemin
                enregistrer_logo_db(equipe, ligue, chemin)
                logger.success(f"[{i}/{total}] ✅ {equipe} ({ligue})")
            else:
                logger.warning(f"[{i}/{total}] ❌ {equipe} ({ligue})")

    logger.success(f"{len(resultats)}/{total} logos téléchargés avec succès")
    return resultats