import json
from django.shortcuts import render
from django.http import JsonResponse
from . import data
from .data import LEAGUE_FLAGS, LEAGUE_COLORS


def home(request):
    # Page d'accueil : KPIs globaux + top buteurs + comparaison ligues
    kpis       = data.get_kpis()
    top_buts   = data.get_top_buteurs(limit=10)
    home_away  = data.get_home_away_stats()
    comp       = data.get_comparaison_ligues()
    ligues     = data.get_ligues()

    # Enrichir avec drapeaux et couleurs
    for item in home_away:
        item['flag']  = LEAGUE_FLAGS.get(item['ligue'], '')
        item['color'] = LEAGUE_COLORS.get(item['ligue'], '#333')

    for item in comp:
        item['flag']  = LEAGUE_FLAGS.get(item['ligue'], '')
        item['color'] = LEAGUE_COLORS.get(item['ligue'], '#333')

    # Données JSON pour les graphiques Chart.js
    # Calculer les pourcentages pour le graphique
    for h in home_away:
        t = h['total_matchs'] or 1
        h['pct_dom'] = round(h['victoires_dom'] / t * 100, 1)
        h['pct_nul'] = round(h['nuls'] / t * 100, 1)
        h['pct_ext'] = round(h['victoires_ext'] / t * 100, 1)
    home_away_json = json.dumps(home_away)
    comp_json      = json.dumps([{
        'ligue':      r['ligue'],
        'moy_buts':   round(r['moy_buts_marques'] or 0, 1),
        'possession': round(r['moy_possession'] or 0, 1),
        'color':      LEAGUE_COLORS.get(r['ligue'], '#333'),
    } for r in comp])

    return render(request, 'dashboard/home.html', {
        'kpis':          kpis,
        'top_buts':      top_buts,
        'home_away':     home_away,
        'home_away_json': home_away_json,
        'comp_json':     comp_json,
        'ligues':        ligues,
        'flags':         LEAGUE_FLAGS,
    })


def ligue(request, nom_ligue):
    # Page détail d'une ligue : classement + buts/journée + résultats
    classement    = data.get_classement(ligue=nom_ligue)
    resultats     = data.get_resultats(ligue=nom_ligue, limit=60)
    buts_journee  = data.get_buts_par_journee(ligue=nom_ligue)
    top_buts      = data.get_top_buteurs(limit=10, ligue=nom_ligue)
    top_passes    = data.get_top_passeurs(limit=10, ligue=nom_ligue)
    stats_equipes = data.get_stats_equipes(ligue=nom_ligue)
    ligues        = data.get_ligues()

    # Données pour graphique évolution buts/journée
    buts_chart = json.dumps({
        'labels': [str(r['semaine']) for r in buts_journee],
        'data':   [r['total_buts'] for r in buts_journee],
    })

    # Données pour bubble chart possession vs buts
    equipes_chart = json.dumps([{
        'label': r['equipe'],
        'x':     round(r['possession'] or 0, 1),
        'y':     r['buts_marques'] or 0,
        'r':     max(4, (r['buts_marques'] or 0) / 3),
    } for r in stats_equipes])

    return render(request, 'dashboard/ligue.html', {
        'nom_ligue':     nom_ligue,
        'flag':          LEAGUE_FLAGS.get(nom_ligue, ''),
        'color':         LEAGUE_COLORS.get(nom_ligue, '#333'),
        'classement':    classement,
        'resultats':     resultats,
        'buts_chart':    buts_chart,
        'top_buts':      top_buts,
        'top_passes':    top_passes,
        'equipes_chart': equipes_chart,
        'ligues':        ligues,
    })


def joueurs(request):
    # Page joueurs : filtrage par ligue et poste
    ligue_filtre = request.GET.get('ligue', '')
    poste_filtre = request.GET.get('poste', '')
    tri          = request.GET.get('tri', 'buts')
    ligues       = data.get_ligues()

    # Récupérer les joueurs selon filtre
    top_buts   = data.get_top_buteurs(limit=50, ligue=ligue_filtre if ligue_filtre else None)
    top_passes = data.get_top_passeurs(limit=50, ligue=ligue_filtre if ligue_filtre else None)

    # Filtrer par poste si demandé
    if poste_filtre:
        top_buts   = [j for j in top_buts   if poste_filtre in (j.get('poste') or '')]
        top_passes = [j for j in top_passes if poste_filtre in (j.get('poste') or '')]

    # Choisir la liste selon le tri
    joueurs_list = top_buts if tri == 'buts' else top_passes

    return render(request, 'dashboard/joueurs.html', {
        'joueurs':       joueurs_list,
        'ligues':        ligues,
        'ligue_filtre':  ligue_filtre,
        'poste_filtre':  poste_filtre,
        'tri':           tri,
        'flags':         LEAGUE_FLAGS,
    })


def equipes(request):
    # Page équipes : comparaison offensive / défensive / possession
    ligue_filtre  = request.GET.get('ligue', '')
    ligues        = data.get_ligues()
    stats         = data.get_stats_equipes(ligue=ligue_filtre if ligue_filtre else None)
    classements   = data.get_classement(ligue=ligue_filtre if ligue_filtre else None)

    # Calculer le ratio buts/match pour chaque équipe
    for s in stats:
        matchs = s.get('matchs') or 1
        s['ratio_att']  = round((s.get('buts_marques') or 0) / matchs, 2)
        s['ratio_def']  = round((s.get('buts_encaisses') or 0) / matchs, 2)
        s['diff_buts']  = (s.get('buts_marques') or 0) - (s.get('buts_encaisses') or 0)

    # Top 10 attaques et défenses pour les graphiques
    top_attaques = sorted(stats, key=lambda x: x['ratio_att'], reverse=True)[:10]
    top_defenses = sorted(stats, key=lambda x: x['ratio_def'])[:10]

    # Données JSON pour les graphiques
    att_chart = json.dumps({
        'labels': [r['equipe'] for r in top_attaques],
        'data':   [r['ratio_att'] for r in top_attaques],
        'colors': [LEAGUE_COLORS.get(r['ligue'], '#333') for r in top_attaques],
    })
    def_chart = json.dumps({
        'labels': [r['equipe'] for r in top_defenses],
        'data':   [r['ratio_def'] for r in top_defenses],
        'colors': [LEAGUE_COLORS.get(r['ligue'], '#333') for r in top_defenses],
    })

    return render(request, 'dashboard/equipes.html', {
        'stats':         stats,
        'ligues':        ligues,
        'ligue_filtre':  ligue_filtre,
        'att_chart':     att_chart,
        'def_chart':     def_chart,
        'flags':         LEAGUE_FLAGS,
        'colors':        LEAGUE_COLORS,
    })


def matchs(request):
    # Page résultats : tous les matchs filtrables par ligue
    ligue_filtre = request.GET.get('ligue', '')
    ligues       = data.get_ligues()
    resultats    = data.get_resultats(
        ligue=ligue_filtre if ligue_filtre else None,
        limit=200
    )
    home_away    = data.get_home_away_stats(ligue=ligue_filtre if ligue_filtre else None)

    for item in home_away:
        item['flag']  = LEAGUE_FLAGS.get(item['ligue'], '')
        item['color'] = LEAGUE_COLORS.get(item['ligue'], '#333')

    return render(request, 'dashboard/matchs.html', {
        'resultats':     resultats,
        'ligues':        ligues,
        'ligue_filtre':  ligue_filtre,
        'home_away':     home_away,
        'flags':         LEAGUE_FLAGS,
    })


# --- API JSON pour les requêtes AJAX ---

def api_buts_journee(request):
    # API : buts par journée pour une ligue (graphique dynamique)
    ligue = request.GET.get('ligue')
    data_buts = data.get_buts_par_journee(ligue=ligue)
    return JsonResponse({'data': data_buts})


def api_forme_equipe(request):
    # API : derniers résultats d'une équipe
    equipe = request.GET.get('equipe', '')
    forme  = data.get_forme_equipe(equipe, nb_matchs=8)
    return JsonResponse({'data': forme})
