from bs4 import BeautifulSoup
from loguru import logger

#Importer depuis les fichiers locaux
from browser import charger_page
from settings import LEAGUES, SAISON, STANDING_URL, BASE_URL


def scraper_stats_equipes(ligue_nom: str) -> list:
    #Récupérer les statistiques des équipes d'une ligue
    info = LEAGUES[ligue_nom]
    url = STANDING_URL.format(
        base=BASE_URL,
        lid=info["id"],
        saison=SAISON,
        slug=info["slug"],
    )

    #Charger la page via curl_cffi sans Playwright
    html = charger_page(None, url)

    if not html:
        logger.warning(f"Aucun HTML récupéré pour stats équipes {ligue_nom}")
        return []

    bsoup = BeautifulSoup(html, "html.parser")

    #Chercher la table des stats standards des équipes
    table = None
    for t in bsoup.find_all("table"):
        tid = t.get("id", "")
        if "stats_squads_standard_for" in tid:
            table = t
            break

    if table is None:
        #Chercher une table alternative si la première n'existe pas
        for t in bsoup.find_all("table"):
            tid = t.get("id", "")
            if "squad" in tid and "standard" in tid:
                table = t
                break

    if table is None:
        logger.warning(f"Table stats équipes introuvable pour {ligue_nom}")
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

        equipe = val("team")
        if not equipe:
            continue

        rows.append({
            "equipe":         equipe,
            "ligue":          ligue_nom,
            "matchs":         val_int("games"),
            "buts_marques":   val_int("goals"),
            "buts_encaisses": val_int("goals_against"),
            "xg":             val_float("xg"),
            "xga":            val_float("xga"),
            "possession":     val_float("possession"),
            "saison":         SAISON,
        })

    logger.success(f"Stats équipes {ligue_nom} : {len(rows)} équipes récupérées")
    return rows