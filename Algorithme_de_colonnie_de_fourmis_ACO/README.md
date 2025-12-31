# Projet : Algorithme de colonie de fourmis (Ant Colony Optimization – ACO)

## Contexte
Ce projet s’inscrit dans le cadre du projet tutoré (PTUT) SAE3-01.  
Il porte sur l’étude et la simulation d’un algorithme inspiré de la nature, l’algorithme de colonie de fourmis (Ant Colony Optimization – ACO), utilisé pour la résolution de problèmes complexes de recherche de chemin optimal.

Les algorithmes de colonies de fourmis reposent sur l’observation de comportements simples présents dans la nature. Combinés collectivement, ces comportements permettent de faire émerger des solutions efficaces sans connaissance globale de l’environnement.

Dans ce projet, l’algorithme est appliqué à un environnement discret représenté sous forme de grille. L’objectif est de déterminer un chemin reliant un point de départ (le nid) à un point d’arrivée (la nourriture), en tenant compte de la présence d’obstacles et de zones difficiles à traverser. Cette approche est ensuite illustrée dans un contexte plus concret, correspondant à la recherche du plus court chemin entre une salle de classe et le restaurant universitaire.

---

## Problématique
Comment un ensemble d’agents simples, disposant uniquement d’informations locales, peut-il faire émerger collectivement un chemin optimal dans un environnement contraint, sans disposer d’une connaissance globale de l’espace étudié ?

---

## Démarche

### 1. Modélisation du problème
- Représentation de l’environnement sous forme de grille discrète.
- Définition de cases obstacles non franchissables.
- Définition de zones difficiles associées à un coût de traversée plus élevé.
- Identification du nid et de la nourriture comme points de départ et d’arrivée.
- Prise en compte d’un coût global combinant distance parcourue et contraintes environnementales.

### 2. Principe de l’algorithme de colonie de fourmis
- Simulation du comportement collectif des fourmis basé sur :
  - l’exploration probabiliste,
  - le dépôt de phéromones,
  - l’évaporation progressive des phéromones.
- Renforcement progressif des chemins les plus courts ou les moins coûteux.
- Émergence d’un chemin dominant sans calcul direct de la solution optimale.

### 3. Implémentation et architecture du projet
- Mise en place d’une architecture modulaire afin de séparer clairement les responsabilités :
  - gestion de la simulation,
  - comportement des fourmis,
  - gestion des phéromones,
  - paramètres globaux,
  - affichage graphique.
- Organisation du code facilitant la lisibilité, la maintenance et l’évolution du projet.

### 4. Simulation et analyse
- Exécution de plusieurs scénarios avec variations :
  - du nombre d’obstacles,
  - du coût des zones difficiles,
  - des paramètres de l’algorithme.
- Observation de la convergence progressive vers un chemin stable reliant le nid à la nourriture.

---

## Compétences développées
- Modélisation de problèmes complexes dans un environnement discret.
- Compréhension et implémentation d’algorithmes inspirés de la nature.
- Programmation modulaire et structurée en Python.
- Analyse du comportement d’un algorithme probabiliste.
- Esprit critique sur les performances et les limites des méthodes d’optimisation.

---

## Outils utilisés
- Python pour l’implémentation de l’algorithme et la simulation.
- Programmation orientée objet.
- Outils de visualisation graphique pour l’analyse des trajectoires et des phéromones.
- Environnement de développement Python.

---

## Résultats
- Simulation fonctionnelle illustrant le comportement collectif des fourmis.
- Mise en évidence de l’émergence progressive d’un chemin optimal entre le nid et la nourriture.
- Visualisation claire de l’impact des obstacles, des zones difficiles et des paramètres sur la convergence.
- Analyse des avantages et des limites de l’algorithme de colonie de fourmis dans des environnements contraints.

---

## Quelques visualisations illustratives

### Environnement de simulation et architecture du projet
![Architecture et environnement de simulation](Portfolio-Projets-DataScience/Algorithme_de_colonnie_de_fourmis_ACO/Capture d'écran 2025-12-24 113419.png)

### Émergence du chemin optimal
![Chemin optimal et évolution des phéromones](Algorithme_de_colonnie_de_fourmis_ACO/im10.png)

