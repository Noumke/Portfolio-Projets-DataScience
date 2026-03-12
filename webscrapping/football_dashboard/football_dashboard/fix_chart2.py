with open('templates/dashboard/home.html', 'r', encoding='utf-8') as f:
    content = f.read()

old = '''        datasets: [
            {
                label: '🏠 Domicile',
                data: homeAwayData.map(d => d.victoires_dom),
                backgroundColor: '#10b981',
                borderRadius: 4,
            },
            {
                label: '🤝 Nul',
                data: homeAwayData.map(d => d.nuls),
                backgroundColor: '#6b7280',
                borderRadius: 4,
            },
            {
                label: '✈️ Extérieur',
                data: homeAwayData.map(d => d.victoires_ext),
                backgroundColor: '#f59e0b',
                borderRadius: 4,
            },
        ]'''

new = '''        datasets: [
            {
                label: '🏠 Domicile',
                data: homeAwayData.map(d => d.pct_dom),
                backgroundColor: '#10b981',
                borderRadius: 4,
            },
            {
                label: '🤝 Nul',
                data: homeAwayData.map(d => d.pct_nul),
                backgroundColor: '#6b7280',
                borderRadius: 4,
            },
            {
                label: '✈️ Extérieur',
                data: homeAwayData.map(d => d.pct_ext),
                backgroundColor: '#f59e0b',
                borderRadius: 4,
            },
        ]'''

content = content.replace(old, new)

# Ajouter le symbole % sur l'axe Y
content = content.replace(
    "y: { stacked: true, grid: { color: '#2a3550' } }",
    "y: { stacked: true, max: 100, grid: { color: '#2a3550' }, ticks: { callback: v => v + '%' } }"
)

with open('templates/dashboard/home.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('home.html OK')
