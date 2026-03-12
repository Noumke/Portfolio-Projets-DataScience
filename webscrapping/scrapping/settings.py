import os

#Délais minimum et maximum entre chaque requête (en secondes)
DELAY_MIN = 4
DELAY_MAX = 8

#Saison cible du projet
SAISON = "2024-2025"

#Ligues disponibles avec leurs identifiants et slugs FBref
LEAGUES = {
    "Premier League": {"id": "9",  "slug": "Premier-League"},
    "La Liga":        {"id": "12", "slug": "La-Liga"},
    "Serie A":        {"id": "11", "slug": "Serie-A"},
    "Ligue 1":        {"id": "13", "slug": "Ligue-1"},
    "Bundesliga":     {"id": "20", "slug": "Bundesliga"},
}

#URL racine du site FBref
BASE_URL = "https://fbref.com"

#URL de la page classement et stats générales d'une ligue
STANDING_URL = "{base}/en/comps/{lid}/{saison}/{saison}-{slug}-Stats"

#URL de la page des scores et calendrier des matchs
FIXTURE_URL = "{base}/en/comps/{lid}/{saison}/schedule/{saison}-{slug}-Scores-and-Fixtures"

#URL de la page des statistiques standards des joueurs
PLAYER_STATS_URL = "{base}/en/comps/{lid}/{saison}/stats/{saison}-{slug}-Stats"

#URL du modèle de photo des joueurs
HEADSHOT_URL = "https://fbref.com/req/202302030/images/headshots/{player_id}_2022.jpg"

#Chemin vers la base de données dans le dossier courant
DB_PATH = "football.db"

#Dossier de sauvegarde des images joueurs
IMAGES_DIR = os.path.join("images", "players")

#Dossier de sauvegarde des logos des clubs
LOGOS_DIR = os.path.join("images", "logos")