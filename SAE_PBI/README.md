# Projet : Analyse de données, reporting et datavisualisation – SNCF

## Contexte
Ce projet s’appuie sur un jeu de données fourni par la SNCF concernant la fréquentation annuelle des gares françaises (montées et descentes) entre 2015 et 2022.  
Les données ont été enrichies avec des informations géographiques, socio-économiques et immobilières pour chaque commune, ainsi que les types de trains desservant les gares.  
L’objectif est de comprendre les dynamiques régionales et l’impact du trafic ferroviaire sur la fréquentation des gares et le marché immobilier.

## Problématique
> Quel est l'impact du trafic ferroviaire sur les dynamiques régionales, notamment en termes de fréquentation des gares, d'évolution du nombre de voyageurs et du marché immobilier ?

## Démarche
### 1. Choix et analyse des données
- Sélection des colonnes pertinentes : code géographique, code département, code unique de la gare, code postal, longitude/latitude, nombre de voyageurs (2015-2022), nombre de départs par type de train, prix médian au m².  
- Utilisation d’un dictionnaire des colonnes pour interpréter correctement les données.  
- Intégration d’une base complémentaire contenant des informations sur les régions et codes départementaux.  
- Création de tables via DAX pour structurer les données et améliorer la pertinence des visualisations.

### 2. Nettoyage et préparation des données
- Vérification et correction des colonnes numériques, gestion des espaces et des séparateurs incorrects.  
- Script Python pour extraire et nettoyer les données : suppression des espaces, correction des types de données, nettoyage des noms de gares.  
- Export des données nettoyées dans un fichier `Problematique_liees_a_la_gare.csv` prêt pour l’analyse.

### 3. Visualisation et reporting
- Création de datavisualisations pour répondre à la problématique : cartes, graphiques de fréquentation, évolution du nombre de voyageurs et relation avec les prix immobiliers.  
- Présentation des résultats dans un rapport PDF ou PowerPoint détaillant le contexte, la démarche, les choix effectués et les difficultés rencontrées.

## Compétences développées
- Analyse et traitement de données massives.  
- Nettoyage et préparation des données avec Python et Power BI.  
- Création de datavisualisations pertinentes pour répondre à une problématique métier.  
- Structuration et organisation de données pour améliorer la qualité des analyses.  
- Reporting et communication des résultats.

## Outils utilisés
- Python pour le traitement, le nettoyage la structuration des données.  
- Power BI pour la visualisation des données.  
- Excel pour vérification et enrichissement des données.  
- Outils géographiques pour l’intégration des données régionales et des codes départementaux.

## Résultats
- Jeu de données propre et structuré prêt à l’analyse.  
- Datavisualisations illustrant l’impact du trafic ferroviaire sur les gares et le marché immobilier.  
- Rapport final présentant le contexte, la démarche, les résultats et les conclusions.

## Quelques visualisations illustratifs
![le nombre de depart du type de Train par année]([https://mon-site.com/graphique.png](https://drive.google.com/file/d/1mNL0sYYbdCR7S3v2UKxeMPb5JIMRCSnd/view?usp=drive_link))


