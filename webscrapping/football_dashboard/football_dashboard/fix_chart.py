import json

# Modifier views.py pour envoyer des pourcentages
with open('dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '    home_away_json = json.dumps(home_away)'
new = '''    # Calculer les pourcentages pour le graphique
    for h in home_away:
        t = h['total_matchs'] or 1
        h['pct_dom'] = round(h['victoires_dom'] / t * 100, 1)
        h['pct_nul'] = round(h['nuls'] / t * 100, 1)
        h['pct_ext'] = round(h['victoires_ext'] / t * 100, 1)
    home_away_json = json.dumps(home_away)'''

content = content.replace(old, new)
with open('dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('views.py OK')
