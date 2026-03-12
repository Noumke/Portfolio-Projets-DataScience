with open('dashboard/data.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''def get_stats_equipes(ligue=None):
    # Stats des équipes avec possession et buts
    conn = get_conn()
    if ligue:
        rows = conn.execute("""
            SELECT e.equipe, e.ligue, e.matchs, e.buts_marques, e.buts_encaisses,
                   e.possession, l.chemin as logo
            FROM stats_equipes e
            LEFT JOIN logos_clubs l ON l.equipe = e.equipe AND l.ligue = e.ligue
            WHERE e.ligue = ?
            ORDER BY e.buts_marques DESC
        """, (ligue,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT e.equipe, e.ligue, e.matchs, e.buts_marques, e.buts_encaisses,
                   e.possession, l.chemin as logo
            FROM stats_equipes e
            LEFT JOIN logos_clubs l ON l.equipe = e.equipe AND l.ligue = e.ligue
            ORDER BY e.buts_marques DESC
        """).fetchall()
    conn.close()'''

new = '''def get_stats_equipes(ligue=None):
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
    conn.close()'''

content = content.replace(old, new)
with open('dashboard/data.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('data.py corrige OK')
