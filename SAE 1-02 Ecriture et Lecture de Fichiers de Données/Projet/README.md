# Projet : SAE Lecture et Écriture de fichiers – Données hospitalières

## Contexte
Le projet consiste à développer un programme Python capable de **lire, transformer et écrire des données** issues de fichiers CSV hospitaliers.  
L’objectif est de migrer les données d’un système source vers un nouveau système cible, tout en respectant les spécifications de format et en documentant toutes les modifications effectuées.

## Objectifs
- Nettoyer et transformer les données issues des fichiers `hospital_data.csv` et `additional_hospital_data.csv`.  
- Ajouter des informations calculées (âge, statut).  
- Fusionner les fichiers et gérer les doublons.  
- Générer un log des modifications pour assurer la traçabilité.

## Démarche

### 1. Lecture des fichiers
- Les deux fichiers CSV sont lus à l’aide de la bibliothèque **pandas**, adaptée à la manipulation de données tabulaires.

### 2. Conversion et formatage des dates
- Les colonnes `DOB` et `LastVisit` sont converties en objets datetime (`pd.to_datetime`) et formatées au format `DD/MM/YYYY`.

### 3. Gestion des valeurs manquantes
- Les valeurs manquantes dans la colonne `Diagnosis` sont remplacées par la valeur la plus fréquente (`mode()`), garantissant la cohérence des données.

### 4. Ajout de nouvelles colonnes
- **Age** : calculé à partir de la date de naissance.  
- **Statut** : “Sain” si le diagnostic est HEALTHY, sinon “Malade”, via une fonction lambda appliquée à chaque élément de la colonne `Diagnosis`.

### 5. Standardisation des diagnostics
- La colonne `Diagnosis` est mise en majuscules (`str.upper()`) pour uniformiser les données et faciliter les analyses.

### 6. Fusion des fichiers et gestion des doublons
- Les deux jeux de données sont fusionnés avec `pd.concat()`.  
- Les doublons sur la colonne `PatientID` sont supprimés (`drop_duplicates()`).

### 7. Génération du log
- Un fichier `modifications_log.txt` recense toutes les modifications effectuées : conversions de dates, remplissage de valeurs manquantes, ajout de colonnes, suppression des doublons.

## Compétences développées
- Lecture et écriture de fichiers CSV avec Python.  
- Nettoyage et transformation des données (dates, valeurs manquantes, colonnes calculées).  
- Fusion et déduplication de jeux de données.  
- Traçabilité des modifications via un log.  
- Documentation et structuration de code Python.

## Outils utilisés
- Python (bibliothèque pandas) pour le traitement des données.  
- Fichiers CSV comme format source et cible.  
- Fichier texte pour le log des modifications.

## Résultats
- Fichiers CSV nettoyés et transformés selon les spécifications.  
- Fusion des deux fichiers sans doublons.  
- Colonne `Age` et `Statut` ajoutées.  
- Log des modifications généré pour assurer la traçabilité.
