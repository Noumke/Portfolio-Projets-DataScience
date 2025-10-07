import json

FICHIER_JSON  = "script.json"

def lire_donnees():
    with open(FICHIER_JSON, 'r', encoding = 'utf-8') as f:
        return json.load(f)

def ecrire_donnees(donnees):
    with open(FICHIER_JSON, 'w', encoding = 'utf-8') as f:
        json.dump(donnees, f, indent = 4, ensure_ascii = False)