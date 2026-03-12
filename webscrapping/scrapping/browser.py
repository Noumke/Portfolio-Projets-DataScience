import time
import random
from playwright.sync_api import sync_playwright, Page
from loguru import logger

#Importer les constantes depuis settings local
from settings import DELAY_MIN, DELAY_MAX

#User agent mobile qui passe mieux Cloudflare que le desktop
USER_AGENT_MOBILE = (
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/145.0.0.0 Mobile Safari/537.36"
)


def charger_page(page, url: str) -> str:
    #Charger une page via Playwright avec attente Cloudflare et retourner son HTML
    wait = random.uniform(DELAY_MIN, DELAY_MAX)
    logger.info(f"Attente de {wait:.1f}s avant chargement...")
    time.sleep(wait)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,              #Visible pour passer Cloudflare
            args=[
                "--disable-blink-features=AutomationControlled",
                "--start-maximized",
                "--no-sandbox",
            ]
        )

        context = browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="fr-FR",
            user_agent=USER_AGENT_MOBILE,  #Mobile passe mieux Cloudflare
        )

        page = context.new_page()

        #Masquer la propriété webdriver pour contourner la détection
        page.add_init_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

        logger.info(f"Chargement : {url}")
        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        #Attendre 30 secondes que Cloudflare passe automatiquement
        logger.info("Attente passage Cloudflare (30s)...")
        page.wait_for_timeout(30000)

        html = page.content()

        #Si la page est encore trop courte, attendre 30s supplémentaires
        if len(html) < 100000:
            logger.warning("Page trop courte, attente 30s supplémentaires...")
            page.wait_for_timeout(30000)
            html = page.content()

        browser.close()

    logger.success(f"Page récupérée : {len(html)} caractères")
    return html


def attendre_aleatoire() -> None:
    #Pause aléatoire entre deux requêtes consécutives
    attente = random.uniform(DELAY_MIN, DELAY_MAX)
    logger.debug(f"Pause de {attente:.1f}s...")
    time.sleep(attente)