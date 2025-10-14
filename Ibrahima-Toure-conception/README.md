# Projet : Conception d’une base de données pour une banque clermontoise

## Contexte
La petite banque clermontoise, avec une seule agence, fonctionnait jusqu’ici avec des outils rudimentaires.  
La gestion des comptes se faisait dans un fichier CSV (`gestion_bancaire.csv`).  

Le projet consiste à **concevoir et mettre en place une base de données relationnelle** permettant de structurer et gérer les informations clients et comptes, tout en répondant aux besoins spécifiques de la banque.

## Objectifs du projet
- Structurer les données clients et comptes dans une base relationnelle PostgreSQL.  
- Permettre la gestion des comptes associés à plusieurs clients (comptes communs ou associatifs).  
- Suivre les mouvements financiers (date, montant, type de transaction, parties concernées).  
- Assurer le suivi des agents responsables pour chaque client.  
- Gérer les programmes de parrainage avec historique des actions et mouvements associés.  
- Créer des vues répondant à des besoins spécifiques du directeur (comptes dormants, état des parrainages).

## Démarche
1. Analyse des besoins du directeur de la banque et extraction des informations depuis le fichier CSV existant.  
2. Conception du **Modèle Conceptuel de Données (MCD)** pour représenter clients, comptes, agents, mouvements et parrainages.  
3. Transformation en **schéma relationnel** respectant les règles de normalisation.  
4. Création des **tables PostgreSQL** et alimentation initiale avec les données CSV.  
5. Création de **vues spécifiques** pour :  
   - Comptes dormants (clients avec date du dernier mouvement < 31/12 de l’année précédente).  
   - État des parrainages (historique depuis le 01/01 de l’année).  
6. Export des vues au format CSV pour utilisation dans Excel.  

## Compétences développées
- Modélisation conceptuelle et logique des données.  
- Normalisation et gestion des relations complexes (comptes multiples, rôles des clients dans une association).  
- SQL avancé : création de tables, vues, scripts d’alimentation et d’exportation.  
- Analyse de données et mise en place de solutions adaptées aux besoins métier.  
- Gestion de projet : de l’analyse des besoins à la mise en production d’une base structurée.

## Outils utilisés
- PostgreSQL pour la création et gestion de la base de données.  
- SQL pour les scripts de création, alimentation, exportation et création de vues.  
- Excel pour l’import/export et vérification des données.  
- Logiciels de modélisation (Mocodo) pour le MCD.

## Résultats
- Base de données relationnelle fonctionnelle et normalisée.  
- Vues spécifiques pour les comptes dormants et état des parrainages, exportables en CSV.  
- Documentation complète du projet (rapport de 6 pages) détaillant toutes les étapes de création, le MCD, le schéma relationnel, les scripts SQL et les vues.

