import os
import time
import random
import sqlite3
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from loguru import logger
from playwright.sync_api import sync_playwright

#Importer depuis le fichier settings local
from settings import HEADSHOT_URL, IMAGES_DIR, DB_PATH

#Nombre de téléchargements simultanés
NB_WORKERS = 5

#Agent utilisateur mobile
USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Mobile Safari/537.36"
)


def recuperer_cookies_fbref() -> dict:
    #Ouvrir un navigateur une seule fois pour récupérer les cookies FBref
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
        for cookie in context.cookies():
            cookies_dict[cookie["name"]] = cookie["value"]

        browser.close()

    logger.success(f"✅ {len(cookies_dict)} cookies récupérés")
    return cookies_dict


def telecharger_image(args: tuple) -> tuple[str, str, str | None]:
    #Télécharger une image joueur avec requests en utilisant les cookies FBref
    player_id, joueur, cookies = args

    if not player_id or player_id == "nan":
        return player_id, joueur, None

    os.makedirs(IMAGES_DIR, exist_ok=True)

    nom_fichier = f"{player_id}_{joueur.replace(' ', '_').lower()}.jpg"
    chemin_local = os.path.join(IMAGES_DIR, nom_fichier)

    #Vérifier si l'image existe déjà sur le disque
    if os.path.exists(chemin_local):
        return player_id, joueur, chemin_local

    url_image = HEADSHOT_URL.format(player_id=player_id)

    #Pause courte pour ne pas surcharger FBref
    time.sleep(random.uniform(0.3, 0.8))

    headers = {
        "User-Agent": USER_AGENT,
        "Referer": "https://fbref.com/en/",
        "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    }

    for tentative in range(3):
        try:
            response = requests.get(
                url_image,
                headers=headers,
                cookies=cookies,
                timeout=15
            )

            if response.status_code == 200 and len(response.content) > 1000:
                with open(chemin_local, "wb") as f:
                    f.write(response.content)
                return player_id, joueur, chemin_local

            elif response.status_code == 404:
                #Image inexistante sur FBref, pas besoin de réessayer
                return player_id, joueur, None

            else:
                time.sleep(3)

        except Exception as e:
            logger.warning(f"Tentative {tentative + 1}/3 échouée pour {joueur} : {e}")
            time.sleep(5)

    return player_id, joueur, None


def telecharger_toutes_images() -> dict:
    #Télécharger toutes les images en parallèle avec les cookies FBref
    resultats = {}

    if not os.path.exists(DB_PATH):
        logger.error(f"Base de données introuvable : {DB_PATH}")
        return resultats

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #Sélectionner uniquement les joueurs pas encore traités (ni téléchargés ni marqués sans photo)
    cursor.execute("""
        SELECT DISTINCT player_id, joueur
        FROM stats_joueurs
        WHERE player_id IS NOT NULL AND player_id != ''
          AND player_id NOT IN (
              SELECT player_id FROM images_joueurs
          )
    """)
    joueurs = cursor.fetchall()
    conn.close()

    total = len(joueurs)
    logger.info(f"{total} images à télécharger")

    if total == 0:
        logger.success("✅ Toutes les images sont déjà traitées !")
        return resultats

    #Récupérer les cookies via Playwright une seule fois
    cookies = recuperer_cookies_fbref()

    #Préparer les arguments pour chaque worker
    args_list = [(pid, nom, cookies) for pid, nom in joueurs]

    #Télécharger en parallèle avec les cookies
    with ThreadPoolExecutor(max_workers=NB_WORKERS) as executor:
        futures = {
            executor.submit(telecharger_image, args): args
            for args in args_list
        }

        for i, future in enumerate(as_completed(futures), start=1):
            player_id, joueur, chemin = future.result()

            if chemin:
                resultats[player_id] = chemin
                #Enregistrer l'image téléchargée avec telecharge = 1
                conn = sqlite3.connect(DB_PATH)
                conn.execute("""
                    INSERT OR REPLACE INTO images_joueurs
                    (player_id, joueur, chemin, telecharge)
                    VALUES (?, ?, ?, 1)
                """, (player_id, joueur, chemin))
                conn.commit()
                conn.close()
                logger.success(f"[{i}/{total}] ✅ {joueur}")
            else:
                #Enregistrer les joueurs sans photo pour ne pas réessayer
                conn = sqlite3.connect(DB_PATH)
                conn.execute("""
                    INSERT OR IGNORE INTO images_joueurs
                    (player_id, joueur, chemin, telecharge)
                    VALUES (?, ?, NULL, 0)
                """, (player_id, joueur))
                conn.commit()
                conn.close()
                logger.warning(f"[{i}/{total}] ❌ {joueur} — marqué sans photo")

    logger.success(f"{len(resultats)}/{total} images téléchargées avec succès")
    return resultats