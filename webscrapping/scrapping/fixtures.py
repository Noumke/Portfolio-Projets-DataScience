from bs4 import BeautifulSoup
from loguru import logger

#Importer depuis les fichiers locaux
from browser import charger_page
from settings import LEAGUES, SAISON, FIXTURE_URL, STANDING_URL, BASE_URL


def scraper_classement(ligue_nom: str) -> list:
    #Récupérer le classement complet d'une ligue sur FBref
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
        logger.warning(f"Aucun HTML récupéré pour classement {ligue_nom}")
        return []

    bsoup = BeautifulSoup(html, "html.parser")

    #Chercher la table du classement général par son identifiant partiel
    table = None
    for t in bsoup.find_all("table"):
        tid = t.get("id", "")
        if "results" in tid and "overall" in tid:
            table = t
            break

    if table is None:
        logger.warning(f"Table classement introuvable pour {ligue_nom}")
        return []

    rows = []
    rang = 0
    for tr in table.find("tbody").find_all("tr"):
        #Ignorer les lignes séparateurs et sous-titres
        if tr.get("class") and ("spacer" in tr.get("class") or "thead" in tr.get("class")):
            continue

        rang += 1

        def val(stat):
            #Extraire la valeur texte d'une cellule par data-stat
            cell = tr.find(["td", "th"], {"data-stat": stat})
            return cell.get_text(strip=True) if cell else ""

        def val_int(stat):
            #Extraire une valeur entière depuis une cellule
            v = val(stat)
            try:
                return int(v)
            except ValueError:
                return 0

        equipe = val("team")
        if not equipe:
            continue

        rows.append({
            "ligue":       ligue_nom,
            "equipe":      equipe,
            "rang":        rang,
            "matchs":      val_int("games"),
            "victoires":   val_int("wins"),
            "nuls":        val_int("ties"),
            "defaites":    val_int("losses"),
            "buts_pour":   val_int("goals_for"),
            "buts_contre": val_int("goals_against"),
            "difference":  val_int("goal_diff"),
            "points":      val_int("points"),
            "saison":      SAISON,
        })

    logger.success(f"Classement {ligue_nom} : {len(rows)} équipes récupérées")
    return rows


def scraper_resultats(ligue_nom: str) -> list:
    #Récupérer tous les résultats de matchs joués d'une ligue
    info = LEAGUES[ligue_nom]
    url = FIXTURE_URL.format(
        base=BASE_URL,
        lid=info["id"],
        saison=SAISON,
        slug=info["slug"],
    )

    #Charger la page via curl_cffi sans Playwright
    html = charger_page(None, url)

    if not html:
        logger.warning(f"Aucun HTML récupéré pour résultats {ligue_nom}")
        return []

    bsoup = BeautifulSoup(html, "html.parser")

    #Chercher la table du calendrier et des scores
    table = None
    for t in bsoup.find_all("table"):
        tid = t.get("id", "")
        if "sched" in tid:
            table = t
            break

    if table is None:
        logger.warning(f"Table résultats introuvable pour {ligue_nom}")
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

        score = val("score")
        if not score or not any(c.isdigit() for c in score):
            continue

        domicile = val("home_team")
        exterieur = val("away_team")
        if not domicile or not exterieur:
            continue

        try:
            xg_dom = float(val("home_xg") or 0)
        except ValueError:
            xg_dom = 0.0

        try:
            xg_ext = float(val("away_xg") or 0)
        except ValueError:
            xg_ext = 0.0

        try:
            sem = int(val("gameweek"))
        except ValueError:
            sem = 0

        rows.append({
            "ligue":      ligue_nom,
            "semaine":    sem,
            "date_match": val("date"),
            "heure":      val("time"),
            "domicile":   domicile,
            "exterieur":  exterieur,
            "score":      score,
            "xg_dom":     xg_dom,
            "xg_ext":     xg_ext,
            "saison":     SAISON,
        })

    logger.success(f"Résultats {ligue_nom} : {len(rows)} matchs récupérés")
    return rows