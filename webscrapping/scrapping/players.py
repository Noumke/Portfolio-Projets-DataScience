import re
from bs4 import BeautifulSoup
from loguru import logger

#Importer depuis les fichiers locaux
from browser import charger_page
from settings import LEAGUES, SAISON, PLAYER_STATS_URL, BASE_URL


def extraire_player_id(balise_a) -> str:
    #Extraire l'identifiant unique du joueur depuis son lien FBref
    if balise_a is None:
        return ""
    href = balise_a.get("href", "")
    match = re.search(r"/en/players/([a-z0-9]+)/", href)
    return match.group(1) if match else ""


def scraper_stats_joueurs(ligue_nom: str) -> list:
    #Récupérer les statistiques standards de tous les joueurs d'une ligue
    info = LEAGUES[ligue_nom]
    url = PLAYER_STATS_URL.format(
        base=BASE_URL,
        lid=info["id"],
        saison=SAISON,
        slug=info["slug"],
    )

    #Charger la page via curl_cffi sans Playwright
    html = charger_page(None, url)

    if not html:
        logger.warning(f"Aucun HTML récupéré pour stats joueurs {ligue_nom}")
        return []

    bsoup = BeautifulSoup(html, "html.parser")

    #Chercher la table des stats standards des joueurs
    table = None
    for t in bsoup.find_all("table"):
        tid = t.get("id", "")
        if "stats_standard" in tid:
            table = t
            break

    if table is None:
        logger.warning(f"Table stats joueurs introuvable pour {ligue_nom}")
        return []

    rows = []
    for tr in table.find("tbody").find_all("tr"):
        #Ignorer les lignes séparateurs et sous-titres
        if tr.get("class") and ("spacer" in tr.get("class") or "thead" in tr.get("class")):
            continue

        def val(stat):
            #Extraire la valeur texte d'une cellule par data-stat
            cell = tr.find(["td", "th"], {"data-stat": stat})
            return cell.get_text(strip=True) if cell else ""

        def val_int(stat):
            #Convertir la cellule en entier
            v = val(stat)
            try:
                return int(v)
            except ValueError:
                return 0

        def val_float(stat):
            #Convertir la cellule en flottant
            v = val(stat)
            try:
                return float(v)
            except ValueError:
                return 0.0

        joueur = val("player")
        if not joueur:
            continue

        #Extraire le player_id depuis le lien du joueur
        cell_joueur = tr.find(["td", "th"], {"data-stat": "player"})
        lien_joueur = cell_joueur.find("a") if cell_joueur else None
        player_id = extraire_player_id(lien_joueur)

        rows.append({
            "player_id":  player_id,
            "joueur":     joueur,
            "nation":     val("nationality"),
            "equipe":     val("team"),
            "ligue":      ligue_nom,
            "age":        val("age"),
            "poste":      val("position"),
            "matchs":     val_int("games"),
            "titulaire":  val_int("games_starts"),
            "minutes":    val_int("minutes"),
            "buts":       val_int("goals"),
            "passes_dec": val_int("assists"),
            "xg":         val_float("xg"),
            "xag":        val_float("xg_assist"),
            "saison":     SAISON,
        })

    logger.success(f"Stats joueurs {ligue_nom} : {len(rows)} joueurs récupérés")
    return rows