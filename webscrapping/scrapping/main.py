import sys
import os
import sqlite3
from loguru import logger

#Ajouter le dossier courant au chemin de recherche Python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

#Importer depuis les fichiers locaux
from db import (
    init_db,
    insert_classement,
    insert_resultats,
    insert_stats_joueurs,
    insert_stats_equipes,
)
from fixtures import scraper_classement, scraper_resultats
from players import scraper_stats_joueurs
from teams import scraper_stats_equipes
from images import telecharger_toutes_images
from logos import telecharger_tous_logos
from settings import LEAGUES, DB_PATH

#Configuration du fichier de logs dans le dossier courant
logger.add("scraping.log", rotation="10 MB", level="INFO")


def ligue_deja_scrapee(nom_ligue: str) -> bool:
    #Vérifier si la ligue a déjà des données en base pour éviter de re-scraper
    try:
        conn = sqlite3.connect(DB_PATH)
        count = conn.execute(
            "SELECT COUNT(*) FROM classements WHERE ligue = ?", (nom_ligue,)
        ).fetchone()[0]
        conn.close()
        return count > 0
    except Exception:
        return False


def scraper_ligue(nom_ligue: str) -> None:
    #Vérifier si la ligue est déjà en base avant de lancer le scraping
    if ligue_deja_scrapee(nom_ligue):
        logger.info(f"⏭️  {nom_ligue} déjà en base — scraping ignoré")
        return

    logger.info(f"=== Début scraping : {nom_ligue} ===")

    logger.info(f"[{nom_ligue}] Scraping classement...")
    classement = scraper_classement(nom_ligue)
    insert_classement(classement)

    logger.info(f"[{nom_ligue}] Scraping résultats...")
    resultats = scraper_resultats(nom_ligue)
    insert_resultats(resultats)

    logger.info(f"[{nom_ligue}] Scraping stats joueurs...")
    stats_j = scraper_stats_joueurs(nom_ligue)
    insert_stats_joueurs(stats_j)

    logger.info(f"[{nom_ligue}] Scraping stats équipes...")
    stats_e = scraper_stats_equipes(nom_ligue)
    insert_stats_equipes(stats_e)

    logger.success(f"=== Scraping terminé : {nom_ligue} ===")


def main() -> None:
    #Initialiser la base de données SQLite
    logger.info("Initialisation de la base de données...")
    init_db()

    #Scraper uniquement les ligues qui ne sont pas encore en base
    for nom_ligue in LEAGUES:
        try:
            scraper_ligue(nom_ligue)
        except Exception as e:
            logger.error(f"Erreur pour {nom_ligue} : {e}")

    #Télécharger les images des joueurs non encore téléchargées
    logger.info("Téléchargement des images joueurs...")
    telecharger_toutes_images()

    #Télécharger les logos des clubs
    logger.info("Téléchargement des logos des clubs...")
    telecharger_tous_logos()

    logger.success("Scraping complet terminé. Base de données prête.")


if __name__ == "__main__":
    main()