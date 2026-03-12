import sqlite3
from pathlib import Path

# Chemin vers la base football.db
DB_PATH = Path(__file__).resolve().parent.parent / 'football.db'


def clean_path(chemin):
    if not chemin:
        return ''
    return chemin.replace(chr(92), '/').replace('images/', '')


def _fix(p):
    if not p: return ''
    return p.replace(chr(92), '/').replace('images/', '')

LEAGUE_FLAGS = {
    "Premier League": "🏴󠁧󠁢󠁥󠁮󠁧󠁿",
    "La Liga":        "🇪🇸",
    "Serie A":        "🇮🇹",
    "Ligue 1":        "🇫🇷",
    "Bundesliga":     "🇩🇪",
}

LEAGUE_COLORS = {
    "Premier League": "#7c3aed",
    "La Liga":        "#f97316",
    "Serie A":        "#3b82f6",
    "Ligue 1":        "#ec4899",
    "Bundesliga":     "#ef4444",
}

def get_conn():
    # Connexion à la base SQLite avec résultats en dict
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_kpis():
    # KPIs globaux pour la page d'accueil
    conn = get_conn()
    total_matchs   = conn.execute("SELECT COUNT(*) FROM resultats").fetchone()[0]
    total_joueurs  = conn.execute("SELECT COUNT(DISTINCT player_id) FROM stats_joueurs").fetchone()[0]
    total_buts     = conn.execute("SELECT SUM(buts) FROM stats_joueurs").fetchone()[0] or 0
    total_equipes  = conn.execute("SELECT COUNT(DISTINCT equipe) FROM classements").fetchone()[0]
    total_passes   = conn.execute("SELECT SUM(passes_dec) FROM stats_joueurs").fetchone()[0] or 0
    conn.close()
    return {
        "total_matchs":  total_matchs,
        "total_joueurs": total_joueurs,
        "total_buts":    total_buts,
        "total_equipes": total_equipes,
        "total_passes":  total_passes,
    }


def get_classement(ligue=None):
    # Classement d'une ligue avec logo du club
    conn = get_conn()
    if ligue:
        rows = conn.execute("""
            SELECT c.rang, c.equipe, c.ligue, c.matchs, c.victoires, c.nuls,
                   c.defaites, c.buts_pour, c.buts_contre, c.difference, c.points,
                   l.chemin as logo
            FROM classements c
            LEFT JOIN logos_clubs l ON l.equipe = c.equipe AND l.ligue = c.ligue
            WHERE c.ligue = ?
            ORDER BY c.rang
        """, (ligue,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT c.rang, c.equipe, c.ligue, c.matchs, c.victoires, c.nuls,
                   c.defaites, c.buts_pour, c.buts_contre, c.difference, c.points,
                   l.chemin as logo
            FROM classements c
            LEFT JOIN logos_clubs l ON l.equipe = c.equipe AND l.ligue = c.ligue
            ORDER BY c.ligue, c.rang
        """).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_top_buteurs(limit=20, ligue=None):
    # Top buteurs avec photo du joueur
    conn = get_conn()
    params = []
    filtre = ""
    if ligue:
        filtre = "AND s.ligue = ?"
        params.append(ligue)
    rows = conn.execute(f"""
        SELECT s.player_id, s.joueur, s.equipe, s.ligue, s.buts, s.passes_dec,
               s.matchs, s.minutes, s.poste, s.age,
               i.chemin as photo
        FROM stats_joueurs s
        LEFT JOIN images_joueurs i ON i.player_id = s.player_id
        WHERE s.buts > 0 {filtre}
        ORDER BY s.buts DESC, s.passes_dec DESC
        LIMIT ?
    """, params + [limit]).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_top_passeurs(limit=20, ligue=None):
    # Top passeurs décisifs avec photo
    conn = get_conn()
    params = []
    filtre = ""
    if ligue:
        filtre = "AND s.ligue = ?"
        params.append(ligue)
    rows = conn.execute(f"""
        SELECT s.player_id, s.joueur, s.equipe, s.ligue, s.buts, s.passes_dec,
               s.matchs, s.minutes, s.poste, s.age,
               i.chemin as photo
        FROM stats_joueurs s
        LEFT JOIN images_joueurs i ON i.player_id = s.player_id
        WHERE s.passes_dec > 0 {filtre}
        ORDER BY s.passes_dec DESC, s.buts DESC
        LIMIT ?
    """, params + [limit]).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_stats_equipes(ligue=None):
    # Stats equipes en combinant stats_equipes et classements pour avoir buts_contre
    conn = get_conn()
    if ligue:
        rows = conn.execute("""
            SELECT e.equipe, e.ligue, e.matchs,
                   c.buts_pour as buts_marques,
                   c.buts_contre as buts_encaisses,
                   e.possession, l.chemin as logo
            FROM stats_equipes e
            LEFT JOIN classements c ON c.equipe = e.equipe AND c.ligue = e.ligue
            LEFT JOIN logos_clubs l ON l.equipe = e.equipe AND l.ligue = e.ligue
            WHERE e.ligue = ?
            ORDER BY c.buts_pour DESC
        """, (ligue,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT e.equipe, e.ligue, e.matchs,
                   c.buts_pour as buts_marques,
                   c.buts_contre as buts_encaisses,
                   e.possession, l.chemin as logo
            FROM stats_equipes e
            LEFT JOIN classements c ON c.equipe = e.equipe AND c.ligue = e.ligue
            LEFT JOIN logos_clubs l ON l.equipe = e.equipe AND l.ligue = e.ligue
            ORDER BY c.buts_pour DESC
        """).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_buts_par_journee(ligue=None):
    # Buts totaux par journée (calcul Python pour l'em-dash Unicode)
    conn = get_conn()
    if ligue:
        rows = conn.execute(
            "SELECT semaine, ligue, score FROM resultats WHERE semaine > 0 AND ligue=?", (ligue,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT semaine, ligue, score FROM resultats WHERE semaine > 0"
        ).fetchall()
    conn.close()

    # Agréger par semaine et ligue
    stats = {}
    for row in rows:
        sem  = row['semaine'] if hasattr(row, 'keys') else row[0]
        lig  = row['ligue']   if hasattr(row, 'keys') else row[1]
        score = row['score']  if hasattr(row, 'keys') else row[2]
        if '–' not in str(score):
            continue
        try:
            parts = str(score).split('–')
            buts = int(parts[0].strip()) + int(parts[1].strip())
        except:
            continue
        key = (sem, lig)
        if key not in stats:
            stats[key] = {'semaine': sem, 'ligue': lig, 'total_buts': 0, 'nb_matchs': 0}
        stats[key]['total_buts'] += buts
        stats[key]['nb_matchs'] += 1

    result = sorted(stats.values(), key=lambda x: (x['ligue'], x['semaine']))
    return result


def get_home_away_stats(ligue=None):
    # Statistiques domicile vs extérieur par ligue (calcul Python pour l'em-dash)
    conn = get_conn()
    if ligue:
        rows = conn.execute(
            "SELECT ligue, score FROM resultats WHERE ligue=?", (ligue,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT ligue, score FROM resultats"
        ).fetchall()
    conn.close()

    # Agréger par ligue avec parsing Python
    stats = {}
    for row in rows:
        lig = row['ligue'] if hasattr(row, 'keys') else row[0]
        score = row['score'] if hasattr(row, 'keys') else row[1]
        if '–' not in str(score):
            continue
        try:
            parts = str(score).split('–')
            gd, ge = int(parts[0].strip()), int(parts[1].strip())
        except:
            continue
        if lig not in stats:
            stats[lig] = {'ligue': lig, 'victoires_dom': 0, 'nuls': 0, 'victoires_ext': 0, 'total_matchs': 0}
        if gd > ge:
            stats[lig]['victoires_dom'] += 1
        elif gd == ge:
            stats[lig]['nuls'] += 1
        else:
            stats[lig]['victoires_ext'] += 1
        stats[lig]['total_matchs'] += 1

    return list(stats.values())


def get_resultats(ligue=None, limit=50):
    # Derniers résultats de matchs
    conn = get_conn()
    if ligue:
        rows = conn.execute("""
            SELECT ligue, semaine, date_match, domicile, exterieur, score
            FROM resultats
            WHERE ligue = ? AND score LIKE '%–%'
            ORDER BY date_match DESC, semaine DESC
            LIMIT ?
        """, (ligue, limit)).fetchall()
    else:
        rows = conn.execute("""
            SELECT ligue, semaine, date_match, domicile, exterieur, score
            FROM resultats
            WHERE score LIKE '%–%'
            ORDER BY date_match DESC
            LIMIT ?
        """, (limit,)).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_forme_equipe(equipe, nb_matchs=5):
    # Les N derniers résultats d'une équipe (domicile + extérieur)
    conn = get_conn()
    rows = conn.execute("""
        SELECT date_match, domicile, exterieur, score,
               CASE WHEN domicile = ? THEN 'DOM' ELSE 'EXT' END as lieu
        FROM resultats
        WHERE (domicile = ? OR exterieur = ?) AND score LIKE '%–%'
        ORDER BY date_match DESC
        LIMIT ?
    """, (equipe, equipe, equipe, nb_matchs)).fetchall()
    conn.close()
    resultats = []
    for r in rows:
        r = dict(r)
        # Calculer le résultat pour l'équipe demandée
        try:
            parts = r['score'].split('–')
            gd = int(parts[0].strip())
            ge = int(parts[1].strip())
            if r['lieu'] == 'DOM':
                r['resultat'] = 'V' if gd > ge else ('N' if gd == ge else 'D')
            else:
                r['resultat'] = 'V' if ge > gd else ('N' if gd == ge else 'D')
        except:
            r['resultat'] = '?'
        resultats.append(r)
    return resultats


def get_comparaison_ligues():
    # Comparaison offensive et défensive entre ligues
    conn = get_conn()
    rows = conn.execute("""
        SELECT ligue,
               AVG(buts_marques) as moy_buts_marques,
               AVG(buts_encaisses) as moy_buts_encaisses,
               AVG(possession) as moy_possession,
               SUM(buts_marques) as total_buts,
               COUNT(*) as nb_equipes
        FROM stats_equipes
        GROUP BY ligue
    """).fetchall()
    conn.close()
    rows_out = []
    for r in rows:
        d = dict(r)
        for k in ('logo', 'photo', 'chemin'):
            if d.get(k):
                d[k] = _fix(d[k])
        rows_out.append(d)
    return rows_out


def get_joueur_profil(player_id):
    # Profil complet d'un joueur avec son image
    conn = get_conn()
    row = conn.execute("""
        SELECT s.*, i.chemin as photo
        FROM stats_joueurs s
        LEFT JOIN images_joueurs i ON i.player_id = s.player_id
        WHERE s.player_id = ?
        LIMIT 1
    """, (player_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_ligues():
    # Liste de toutes les ligues disponibles
    conn = get_conn()
    rows = conn.execute("SELECT DISTINCT ligue FROM classements ORDER BY ligue").fetchall()
    conn.close()
    return [r['ligue'] for r in rows]


def get_logo_url(equipe, ligue):
    # Récupérer le chemin du logo d'une équipe
    conn = get_conn()
    row = conn.execute(
        "SELECT chemin FROM logos_clubs WHERE equipe=? AND ligue=?", (equipe, ligue)
    ).fetchone()
    conn.close()
    return row['chemin'] if row else None
