with open('dashboard/data.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '"Premier League": "#3d195b"',
    '"Premier League": "#7c3aed"'
).replace(
    '"La Liga":        "#ee8707"',
    '"La Liga":        "#f97316"'
).replace(
    '"Serie A":        "#024494"',
    '"Serie A":        "#3b82f6"'
).replace(
    '"Ligue 1":        "#091c3e"',
    '"Ligue 1":        "#ec4899"'
).replace(
    '"Bundesliga":     "#d3010c"',
    '"Bundesliga":     "#ef4444"'
)

with open('dashboard/data.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Couleurs mises a jour')
