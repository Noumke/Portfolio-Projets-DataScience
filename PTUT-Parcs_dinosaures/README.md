# Projet : Gestion d’un Parc de Dinosaures (en développement)

## Contexte
Ce projet tutoré, développé en **Python avec Pygame**, consiste à créer un **jeu de gestion d’un parc de dinosaures**.  
L’utilisateur incarne un gestionnaire de parc et doit **nourrir, soigner et interagir avec ses dinosaures**, tout en gérant son capital pour acheter de nouveaux dinosaures et améliorer le parc.  
Le projet est réalisé par notre groupe et est actuellement en cours de développement.

## Objectifs
- Concevoir un **jeu interactif en temps réel** avec différentes mécaniques de gestion.  
- Développer nos compétences en **programmation modulaire**, **organisation du code** et **algorithmique**.  
- Apprendre à utiliser la bibliothèque **Pygame** pour le rendu graphique, la gestion des événements et les animations.

## Démarche et développement

### 1. Programmation modulaire
- Le code totalise 1500 lignes et est divisé en **22 modules**, chacun gérant une fonctionnalité spécifique (dinosaures, menus, salles, déplacements, affichages…).  
- Cette approche facilite la maintenance et le débogage, et permet d’utiliser des variables entre modules de manière structurée.

### 2. Programmation avec Pygame
- Gestion du rendu 2D, des événements clavier, de l’audio et des cycles de jeu.  
- Développement de fonctionnalités interactives : déplacement du joueur, menus, suivi de l’état des dinosaures, affichage des éléments du jeu.

### 3. Gestion des objets
- Utilisation de **dictionnaires** pour représenter les objets du jeu (ex : dinosaures, chemins, salles) au lieu de la programmation orientée objet, pour simplifier la compréhension et la modification du code.

### 4. Défis rencontrés
- **Debugging graphique** : certaines images ou éléments ne s’affichaient pas correctement, nécessitant des vérifications précises.  
- **Système de sauvegarde** : choix entre CSV, JSON ou base de données, avec adaptation du JSON pour gérer les sauvegardes rapides.  
- **Gestion des collisions** : détection des collisions avec `pygame.Rect.colliderect()` et masques pour des formes complexes.

## Fonctionnalités principales
- Gestion en **temps réel** des dinosaures : faim, santé, affection.  
- Achat de nouveaux dinosaures et items auprès du marchand.  
- Navigation dans 20 salles avec interactions variées.  
- Système de collecte de pièces pour acheter et améliorer le parc.  
- Objectif final : acheter le **Roi-Dinosaure** pour terminer la partie.

## Compétences développées
- Programmation modulaire et organisation du code.  
- Programmation en Python avec Pygame.  
- Gestion de données et d’objets via dictionnaires.  
- Débogage et optimisation des programmes interactifs.  
- Gestion du temps réel et des interactions utilisateur.

## Outils utilisés
- **Python** pour la programmation.  
- **Pygame** pour la création du jeu 2D.  
- Dictionnaires pour la gestion des objets et modules du jeu.

## Visuels du jeu
![Visuel du jeu](chemin_vers_ton_image.png)  
*Exemple : le personnage se déplace pour nourrir et soigner les dinosaures, accéder au menu et interagir avec le marchand.*

