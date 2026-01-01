
# Projet : Application de gestion des étudiants, des cours et des notes

## Contexte
Ce projet a pour objectif de concevoir une application de gestion des étudiants, des enseignants, des groupes et des cours, intégrant la saisie et la consultation des notes.  
Il s’inscrit dans un cadre académique et vise à mettre en pratique les principes de la programmation orientée objet, de la conception logicielle et du développement d’interfaces graphiques.

Le programme permet d’administrer les personnes (étudiants et enseignants), de gérer les groupes d’étudiants et leurs cours associés, et d’assurer le calcul et l’affichage des moyennes.  
Afin de rendre ce projet concret et réaliste, son fonctionnement s’inspire de la plateforme Odin utilisée à l’IUT pour la gestion des notes et des enseignements, tout en proposant une version simplifiée et adaptée.

Une interface graphique développée avec JavaFX permet une interaction claire et intuitive, tandis qu’un système d’authentification sécurisé garantit que seules les personnes autorisées peuvent accéder aux fonctionnalités sensibles.

---

## Problématique
Comment concevoir une application fiable et sécurisée permettant de gérer des étudiants, des enseignants, des cours et des notes, tout en respectant les principes de la programmation orientée objet et en offrant une interface graphique simple d’utilisation ?

---

## Démarche

### 1. Modélisation des entités
- Définition d’une classe `Personne` regroupant les attributs communs (nom, prénom, âge).
- Héritage des classes `Etudiant` et `Enseignant` à partir de `Personne`.
- Modélisation des entités `Cours`, `Groupe` et `Note` afin de représenter les relations entre étudiants, cours et enseignants.

### 2. Choix de conception et sécurité
- Encapsulation des données via des attributs privés et des getters/setters.
- Mise en place d’un système d’authentification réservé aux enseignants.
- Chiffrement des mots de passe à l’aide d’une fonction de hachage.
- Restriction de la saisie des notes aux enseignants autorisés ou au professeur référent.

### 3. Architecture du projet
- Séparation claire des responsabilités entre :
  - l’interface graphique (JavaFX),
  - la logique métier (classe `Gestionnaire`),
  - les modèles de données.
- Organisation modulaire facilitant la maintenance et l’évolution du projet.

### 4. Implémentation des fonctionnalités
- Gestion des personnes (étudiants et enseignants).
- Création et gestion des groupes d’étudiants.
- Association des cours aux groupes et désignation des enseignants référents.
- Saisie, consultation et calcul des notes et des moyennes pondérées.
- Affichage des résultats et des bulletins via l’interface graphique.

---

## Compétences développées
- Programmation orientée objet en Java.
- Conception et modélisation d’une application logicielle.
- Gestion des droits et de l’authentification des utilisateurs.
- Implémentation d’exceptions personnalisées pour la gestion des erreurs.
- Développement d’interfaces graphiques avec JavaFX.
- Organisation et structuration d’un projet logiciel.

---

## Outils utilisés
- Java pour le développement de l’application.
- JavaFX pour l’interface graphique.
- Programmation orientée objet (héritage, encapsulation, interfaces).
- Gestion des exceptions personnalisées.
- Structures de données pour la gestion des listes d’étudiants, de cours et de groupes.

---

## Résultats
- Application fonctionnelle permettant la gestion complète des étudiants, des enseignants, des groupes et des cours.
- Système d’authentification sécurisé réservé aux enseignants.
- Saisie et consultation des notes avec contrôle des autorisations.
- Calcul automatique des moyennes pondérées.
- Interface graphique claire et interactive facilitant l’utilisation de l’application.

---

## Limites et améliorations possibles
- Les données sont actuellement stockées en mémoire ; l’ajout d’une base de données permettrait de rendre l’application persistante.
- Une gestion des absences pourrait être intégrée.
- L’ajout d’un mode « étudiant » pour la consultation individuelle des notes constituerait une amélioration pertinente.
