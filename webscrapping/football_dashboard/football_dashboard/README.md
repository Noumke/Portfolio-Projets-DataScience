# ⚽ Football Stats Dashboard — Saison 2024-25

Dashboard Django interactif pour explorer les données des 5 grands championnats européens.

## 📁 Structure du projet

```
football_dashboard/
├── football.db              ← Base de données SQLite (à placer ici)
├── media/                   ← Images joueurs et logos clubs
│   ├── players/             ← images/players/*.jpg → copier ici
│   └── logos/               ← images/logos/*.png  → copier ici
├── dashboard/               ← Application Django
│   ├── data.py              ← Accès base de données
│   ├── views.py             ← Vues / logique
│   └── urls.py              ← Routing
├── templates/dashboard/     ← Pages HTML
└── static/css/style.css     ← Styles
```

## 🚀 Installation et lancement

```bash
# 1. Installer Django (une seule fois)
pip install django

# 2. Copier les images joueurs et logos
cp -r images/players/* media/players/
cp -r images/logos/*   media/logos/

# 3. Lancer le serveur
python manage.py runserver

# 4. Ouvrir dans le navigateur
http://127.0.0.1:8000/
```

## 📊 Pages disponibles

| URL | Description |
|-----|-------------|
| `/` | Accueil : KPIs, Top 10 buteurs, comparaison ligues |
| `/ligue/Premier League/` | Classement, buts/journée, stars |
| `/ligue/La Liga/` | Idem pour La Liga |
| `/ligue/Serie A/` | Idem pour Serie A |
| `/ligue/Ligue 1/` | Idem pour Ligue 1 |
| `/ligue/Bundesliga/` | Idem pour Bundesliga |
| `/joueurs/` | Grille joueurs avec photos, filtres par ligue/poste |
| `/equipes/` | Comparaison attaque/défense/possession |
| `/matchs/` | Tous les résultats avec recherche live |

## 🔑 Insights clés (2024-25)

- **Mbappé** domine avec **31 buts** en La Liga
- **Salah** meilleur contributeur total : **29G + 18A = 47**
- **Premier League** : ligue la plus compétitive à l'extérieur (34.7%)
- **Ligue 1** : avantage domicile le plus marqué (46.4%)
- **4 741 buts** au total sur les 5 ligues
