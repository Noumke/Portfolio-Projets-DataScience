# ⚽ Football Stats Dashboard — Saison 2024-25

> Projet complet de **Data Science appliquée au football** : collecte automatique de données depuis FBref via web scraping, stockage SQLite, et visualisation interactive via un tableau de bord Django.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?style=flat-square&logo=django)
![Playwright](https://img.shields.io/badge/Playwright-scraping-orange?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-3-lightblue?style=flat-square&logo=sqlite)
![Chart.js](https://img.shields.io/badge/Chart.js-visualisation-red?style=flat-square)

---

## 🎯 Objectif du projet

Construire un pipeline complet **collecte → stockage → visualisation** pour analyser les performances des 5 grands championnats européens de football sur la saison 2024-25 :

```
FBref.com  →  Scraper Python  →  SQLite  →  Dashboard Django
```

---

## 🏆 Championnats couverts

| Ligue | Pays | Équipes | Matchs |
|-------|------|---------|--------|
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League | Angleterre | 20 | 380 |
| 🇪🇸 La Liga | Espagne | 20 | 380 |
| 🇮🇹 Serie A | Italie | 20 | 380 |
| 🇫🇷 Ligue 1 | France | 18 | 306 |
| 🇩🇪 Bundesliga | Allemagne | 18 | 306 |

---

## 📊 Chiffres clés

| Métrique | Valeur |
|----------|--------|
| ⚽ Buts marqués | **4 741** |
| 🏟️ Matchs joués | **2 136** |
| 👤 Joueurs trackés | **2 773** |
| 🛡️ Clubs | **96** |
| 🎯 Passes décisives | **3 391** |
| 📸 Photos joueurs | **2 533** |

---

## 🗂️ Structure du projet

```
webscrapping/
│
├── 📁 scrapping/                 # Partie 1 — Collecte des données
│   ├── main.py                   # Orchestrateur principal
│   ├── settings.py               # Configuration ligues et URLs
│   ├── browser.py                # Playwright + anti-Cloudflare
│   ├── fixtures.py               # Classements et résultats
│   ├── players.py                # Statistiques joueurs
│   ├── teams.py                  # Statistiques équipes
│   ├── images.py                 # Photos joueurs
│   ├── logos.py                  # Logos clubs
│   ├── db.py                     # Base SQLite
│   ├── requirements.txt          # Dépendances
│   ├── football.db               # Base de données générée
│   └── images/
│       ├── players/              # 2533 photos joueurs
│       └── logos/                # 96 logos clubs
│
└── 📁 football_dashboard/        # Partie 2 — Visualisation
    ├── run.py                    # Lancement rapide
    ├── manage.py                 # Commande Django
    ├── football.db               # Base de données (copie)
    ├── dashboard/
    │   ├── data.py               # Requêtes SQL
    │   ├── views.py              # Logique des pages
    │   └── urls.py               # Routing
    ├── templates/dashboard/      # Pages HTML
    │   ├── base.html             # Template de base
    │   ├── home.html             # Accueil
    │   ├── ligue.html            # Détail championnat
    │   ├── joueurs.html          # Grille joueurs
    │   ├── equipes.html          # Comparaison équipes
    │   └── matchs.html           # Résultats
    ├── static/css/style.css      # Design dark mode
    └── media/                    # Images servies
        ├── players/
        └── logos/
```

---

## 🚀 Installation complète

### Prérequis
- Python 3.10+
- pip

### 1. Cloner le dépôt
```bash
git clone https://github.com/Noumke/Portfolio-Projets-DataScience.git
cd Portfolio-Projets-DataScience/webscrapping
```

### 2. Installer les dépendances
```bash
pip install -r scrapping/requirements.txt
```

---

## 🕷️ Partie 1 — Lancer le scraping

```bash
cd scrapping

# Installer le navigateur Playwright
playwright install chromium

# Lancer la collecte complète
python main.py
```

> ⚠️ Durée estimée : ** 5 à 8 minutes** (délais anti-Cloudflare inclus).  
> La base `football.db` est déjà fournie -cette étape est optionnelle.

---

## 🖥️ Partie 2 — Lancer le dashboard

```bash
cd football_dashboard/football_dashboard

# Windows — copier les images
xcopy /E /I ..\..\scrapping\images\players media\players
xcopy /E /I ..\..\scrapping\images\logos media\logos

# Mac/Linux — copier les images
cp -r ../../scrapping/images/players media/players
cp -r ../../scrapping/images/logos media/logos

# Lancer le serveur
python manage.py runserver
```

Ouvrir dans le navigateur : **http://127.0.0.1:8000/**

### Lancement rapide (Windows)
```bash
python run.py
# Lance le serveur ET ouvre le navigateur automatiquement
```

---

## 📈 Pages du dashboard

| Page | URL | Contenu |
|------|-----|---------|
| 🏠 Accueil | `/` | KPIs, Top 10 buteurs avec photos, comparaison ligues |
| 🏆 Ligue | `/ligue/Premier League/` | Classement avec logos, buts/journée, stars |
| 👤 Joueurs | `/joueurs/` | Grille filtrable par ligue/poste/tri |
| 🛡️ Équipes | `/equipes/` | Top attaques, défenses, possession |
| 📋 Matchs | `/matchs/` | Tous les résultats, recherche live |

---

## 🔍 Insights clés — Saison 2024-25

### 🥇 Top 5 Buteurs
| Joueur | Club | Ligue | Buts | Assists |
|--------|------|-------|------|---------|
| Kylian Mbappé | Real Madrid | 🇪🇸 La Liga | **31** | 3 |
| Mohamed Salah | Liverpool | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 PL | **29** | 18 |
| Robert Lewandowski | Barcelona | 🇪🇸 La Liga | **27** | 2 |
| Harry Kane | Bayern Munich | 🇩🇪 Bundesliga | **26** | 9 |
| Mateo Retegui | Atalanta | 🇮🇹 Serie A | **25** | 8 |

### 🏠 Avantage Domicile
| Ligue | % Dom. | % Ext. | Équilibre |
|-------|--------|--------|-----------|
| 🇫🇷 Ligue 1 | **46%** | 33% | Faible |
| 🇪🇸 La Liga | 44% | 30% | Faible |
| 🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League | 41% | 35% | Moyen |
| 🇮🇹 Serie A | 40% | 32% | Moyen |
| 🇩🇪 Bundesliga | 38% | **36%** | **Très élevé** |

> 💡 La **Bundesliga** est la ligue la plus équilibrée d'Europe (seulement 2% d'écart).

---

## 🛠️ Stack technique

| Outil | Usage |
|-------|-------|
| **Playwright** | Navigation automatisée + contournement Cloudflare |
| **BeautifulSoup4** | Parsing HTML des tableaux FBref |
| **requests** | Téléchargement images avec cookies |
| **SQLite** | Stockage des données |
| **ThreadPoolExecutor** | Téléchargement parallèle des images |
| **Django 6** | Framework web du dashboard |
| **Chart.js** | Graphiques interactifs (barres, courbes, bulles) |
| **Loguru** | Logging structuré du scraping |

---

## ⚠️ Avertissement légal

Ce projet est réalisé à des fins **éducatives uniquement**.  
Les données proviennent de [FBref.com](https://fbref.com) : Sports Reference LLC.

---

## 👤 Auteur

**Noumke TOURE**  
Étudiant en Data Science — Université Clermont Auvergne  
🔗 [Portfolio GitHub](https://github.com/Noumke/Portfolio-Projets-DataScience)
