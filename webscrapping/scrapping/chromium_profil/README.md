# 🕷️ Football Scraper - FBref 2024-25

> Scripts Python pour collecter automatiquement les données des 5 grands championnats européens depuis [FBref.com](https://fbref.com), avec contournement Cloudflare via Playwright.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-automation-orange?style=flat-square)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-parsing-green?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-stockage-lightblue?style=flat-square&logo=sqlite)

---

## 📦 Ce que le scraper collecte

| Données | Source | Volume |
|---------|--------|--------|
| Classements finaux | Page Stats FBref | 96 lignes |
| Résultats de matchs | Page Fixtures FBref | 2 136 matchs |
| Stats joueurs (buts, assists, xG...) | Page Players FBref | 2 773 joueurs |
| Stats équipes (possession, xG...) | Page Squads FBref | 96 équipes |
| Photos de visage joueurs | CDN FBref | 2 533 images |
| Logos des clubs | CDN FBref | 96 logos |

---

## 🗂️ Structure des fichiers

```
scrapping/
│
├── main.py          # Point d'entrée — orchestre tout le scraping
├── settings.py      # Configuration : ligues, URLs, chemins, délais
├── browser.py       # Playwright : contournement Cloudflare
├── fixtures.py      # Scraping classements + résultats de matchs
├── players.py       # Scraping statistiques joueurs
├── teams.py         # Scraping statistiques équipes
├── images.py        # Téléchargement photos joueurs (parallèle)
├── logos.py         # Téléchargement logos clubs (parallèle)
├── db.py            # Gestion base SQLite (init + insertions)
├── requirements.txt # Dépendances Python
│
├── football.db      # Base de données SQLite générée
└── images/
    ├── players/     # Photos joueurs (.jpg)
    └── logos/       # Logos clubs (.png)
```

---

## ⚙️ Installation

### 1. Cloner le projet
```bash
git clone https://github.com/Noumke/Portfolio-Projets-DataScience.git
cd Portfolio-Projets-DataScience/webscrapping/scrapping
```

### 2. Installer les dépendances Python
```bash
pip install -r requirements.txt
```

### 3. Installer le navigateur Playwright
```bash
playwright install chromium
```

---

## 🚀 Lancement du scraping

```bash
python main.py
```

Le script va automatiquement :
1. Initialiser la base de données `football.db`
2. Scraper les 5 ligues dans l'ordre
3. Télécharger les photos joueurs en parallèle
4. Télécharger les logos des clubs en parallèle
5. Logger toutes les actions dans `scraping.log`

> ⚠️ **Durée estimée : 2 à 4 heures** — des délais aléatoires sont inclus pour éviter d'être bloqué par Cloudflare.

---

## 🛡️ Contournement Cloudflare

FBref est protégé par Cloudflare. Le scraper utilise plusieurs techniques :

```python
# browser.py — techniques anti-détection
- Navigateur visible (headless=False)
- User-Agent mobile réel
- Masquage de la propriété navigator.webdriver
- Délais aléatoires entre chaque requête (4 à 8 secondes)
- Attente automatique de 30 secondes au passage Cloudflare
```

---

## ⚙️ Configuration — `settings.py`

```python
# Modifier les délais entre requêtes
DELAY_MIN = 4   # secondes minimum
DELAY_MAX = 8   # secondes maximum

# Modifier la saison cible
SAISON = "2024-2025"

# Ajouter ou retirer des ligues
LEAGUES = {
    "Premier League": {"id": "9",  "slug": "Premier-League"},
    "La Liga":        {"id": "12", "slug": "La-Liga"},
    "Serie A":        {"id": "11", "slug": "Serie-A"},
    "Ligue 1":        {"id": "13", "slug": "Ligue-1"},
    "Bundesliga":     {"id": "20", "slug": "Bundesliga"},
}
```

---

## 🗃️ Structure de la base de données

```sql
-- Classements par ligue
classements (id, ligue, equipe, rang, matchs, victoires, nuls,
             defaites, buts_pour, buts_contre, difference, points, saison)

-- Résultats de matchs
resultats (id, ligue, semaine, date_match, heure,
           domicile, exterieur, score, xg_dom, xg_ext, saison)

-- Statistiques joueurs
stats_joueurs (id, player_id, joueur, nation, equipe, ligue,
               age, poste, matchs, titulaire, minutes,
               buts, passes_dec, xg, xag, saison)

-- Statistiques équipes
stats_equipes (id, equipe, ligue, matchs, buts_marques,
               buts_encaisses, xg, xga, possession, saison)

-- Images joueurs
images_joueurs (player_id, joueur, chemin, telecharge)

-- Logos clubs
logos_clubs (equipe, ligue, chemin, telecharge)
```

---

## 📋 Logs

Toutes les actions sont enregistrées dans `scraping.log` :

```
2024-03-12 | INFO    | Chargement : https://fbref.com/...
2024-03-12 | SUCCESS | Classement Premier League : 20 équipes récupérées
2024-03-12 | SUCCESS | 760 résultats insérés
2024-03-12 | WARNING | Image introuvable pour X — marqué sans photo
```

---

## 🛠️ Stack technique

| Outil | Usage |
|-------|-------|
| **Playwright** | Navigation headless + contournement Cloudflare |
| **BeautifulSoup4** | Parsing HTML des tableaux FBref |
| **requests** | Téléchargement images avec cookies |
| **SQLite** | Stockage local des données |
| **ThreadPoolExecutor** | Téléchargement parallèle des images |
| **Loguru** | Logging coloré et structuré |

---

## ⚠️ Avertissement légal

Ce projet est réalisé à des fins **éducatives uniquement**.  
Les données appartiennent à [FBref.com](https://fbref.com) - Sports Reference LLC.  
Respectez les conditions d'utilisation du site et limitez la fréquence des requêtes.

---

## 👤 Auteur

**Noumke TOURE** - Etudiant Data Science, Université Clermont Auvergne  
🔗 [Portfolio](https://github.com/Noumke/Portfolio-Projets-DataScience)
