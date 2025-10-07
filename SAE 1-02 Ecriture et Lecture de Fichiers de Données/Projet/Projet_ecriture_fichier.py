import pandas as pd
from  datetime import datetime


chemin_fichier_1= "Desktop\\hospital_data.csv"
chemin_fichier_2="Desktop\\additional_hospital_data.csv"
contenu_fichier_1=pd.read_csv(chemin_fichier_1)
contenu_fichier_2=pd.read_csv(chemin_fichier_2)
#print(contenu_fichier_1.head()) #visualiser les premieres lignes
"""
Initialise une liste pour enregistrer toutes les modifications effectuées 
"""
modification=[] 

"""
Convertit les colonnes 'DOB' et 'LastVisit' en format datetime, puis les reformate 
au format DD/MM/YYYY pour garantir une uniformité dans les données.
"""
# Convertir en datetime les colonnes DOB et LastVisit
contenu_fichier_1['DOB']=pd.to_datetime(contenu_fichier_1['DOB'])  
contenu_fichier_1['LastVisit']=pd.to_datetime(contenu_fichier_1['LastVisit'])  
modification.append("Conversion en datetime")
# Formater les dates DD/MM/YYYY
contenu_fichier_1['DOB']=contenu_fichier_1['DOB'].dt.strftime('%d/%m/%Y') 
contenu_fichier_1['LastVisit']=contenu_fichier_1['LastVisit'].dt.strftime('%d/%m/%Y')  
modification.append("Formattage des dates en DD/MM/YYYY")
#print(contenu_fichier_1)
"""
Mise en majuscules de la colonne 'Diagnosis' pour uniformiser les données.
Cela permet d'éviter les erreurs dues à des variations de casse dans les diagnostics.
"""

# Mettre en majuscule les noms de diagnostiques
contenu_fichier_1['Diagnosis'] = contenu_fichier_1['Diagnosis'].str.upper()  
modification.append("Mise en majuscule des noms de diagnostiques")


"""
Identifie les valeurs manquantes dans la colonne 'Diagnosis' et les remplace
par la valeur la plus fréquente.
"""

# quelles sont les collones qui ont des valeurs manquantes
# print(contenu_fichier_1.isnull().sum())

# Retrouver ces lignes manquantes
ligne_manquante_dans_Diagnosis=contenu_fichier_1[contenu_fichier_1['Diagnosis'].isnull()]

# print(ligne_manquante_dans_Diagnosis) #afficher les lignes manquantes

#remplacer les cellules vides par la valeur la plus frequente
valeur_frequente=contenu_fichier_1['Diagnosis'].mode()[0]
#afficher la valeur la plus frequente
# print(valeur_frequente)

contenu_fichier_1['Diagnosis'].fillna(valeur_frequente,inplace=True) #remplacer les valeurs manquantes par la valeur la plus frequente
modification.append("Remplissage des valeurs manquantes dans diagnotiques avec la valeur la plus frequente")
 
#ajouter une colonne Age qui calcule l'age des patients

"""
Ajoute une colonne "Age" en calculant l'âge des patients à partir de leur date de naissance (DOB).
La colonne 'DOB' est temporairement reconvertie au format datetime pour effectuer le calcul.
"""

"""
Ajoute une colonne "Age" en calculant l'âge des patients à partir de leur année de naissance,
sans modifier la colonne 'DOB' d'origine.
"""
# Créer une copie temporaire pour manipuler DOB sans affecter son format original
dob_temp= pd.to_datetime(contenu_fichier_1['DOB'], format='%d/%m/%Y')
# Calcul de l'âge en années à partir de l'année actuelle et de l'année de naissance
contenu_fichier_1['Age'] = datetime.now().year - dob_temp.dt.year
modification.append("Ajout de la colonne Age calculée en soustrayant l'année de naissance de l'année actuelle")

#affcher la colonne diagnosis et verifier si les valeurs sont bien formater 
# print(contenu_fichier_1['Diagnosis'])

"""
Ajoute une colonne "Statut" pour indiquer si un patient est sain ou malade en fonction 
de la colonne 'Diagnosis'. Si le diagnostic est 'HEALTHY', le statut est 'Sain', sinon 'Malade'.
"""

contenu_fichier_1['Statut']=contenu_fichier_1['Diagnosis'].apply( lambda x:  "Sain"if x=='HEALTHY' else 'Malade')
modification.append("Ajout de la colonne Statut pour savoir si le patient est sain ou malade")
"""
Fusionne les deux fichiers de données et supprime les doublons sur la base de 'PatientID'.
"""

# fusionner les deux fichiers

fusionner_fichier=pd.concat([contenu_fichier_1,contenu_fichier_2])
modification.append("Fusion des fichiers fichiers_hospital_data et additional_hospital_data")
# verifier les doublons
duplication_sur_id=fusionner_fichier[fusionner_fichier.duplicated(subset='PatientID',keep=False)]
modification.append("Verification des doublons")
# supprimer les doublons
fusionner_fichier.drop_duplicates(subset='PatientID',inplace=True)
modification.append("Suppression des doublons sur la colonne PatientID")

# enregistrer le fichier fusionner
fusionner_fichier.to_csv("Desktop\\fusionner_fichier.csv",index=False)

"""
Enregistre toutes les modifications effectuées sur les données dans un fichier log.
"""
#print(fusionner_fichier)

# enregistrer les modifications effectuées
with open("Desktop\\modification_log.txt",'w') as fichier_modification:
    for modifications in modification :
        fichier_modification.write(modifications+'\n')
