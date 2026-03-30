#!/usr/bin/env python
"""
Script pour peupler la base de données avec des données de test.
Données récupérées depuis https://actani.fr/index.php/qui-suis-je/
Site : ACT'ani — Education canine, mantrailing (Cantal, France)
Pour lancer : python scripts/populate_db.py depuis la racine du projet
"""
import os
import sys
import django

# on ajoute le répertoire parent au path Python pour que Django soit trouvable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guerre_animaux.settings')
django.setup()

from django.contrib.auth.models import User
from api.models import Army, Animal, Weapon

# animaux récupérés depuis actani.fr, chaque entrée correspond à un animal réel du site
ACTANI_ANIMALS = [
    {
        "name":      "Shana",
        "breed":     "Chien (race inconnue)",
        "species":   "chien",
        "nickname":  "La plus belle étoile du ciel",
        "image_url": "https://actani.fr/wp-content/uploads/2020/06/playa-20-of-21-1-640x400.jpg",
        "deceased":  True,
    },
    {
        "name":      "Chopin",
        "breed":     "Chien (race inconnue)",
        "species":   "chien",
        "nickname":  "Ramasseur de bâtons professionnel",
        "image_url": "https://actani.fr/wp-content/uploads/2020/06/chopin-640x400.jpg",
        "deceased":  True,
    },
    {
        "name":      "Toundra",
        "breed":     "Chien (race inconnue)",
        "species":   "chien",
        "nickname":  "La terreur",
        "image_url": "https://actani.fr/wp-content/uploads/2021/10/IMG_1372-640x400.jpg",
        "deceased":  False,
    },
    {
        "name":      "Echo",
        "breed":     "Chien (~48 kg)",
        "species":   "chien",
        "nickname":  "Le petit crapaud",
        "image_url": "https://actani.fr/wp-content/uploads/2025/10/503439837_1195682309024867_8292829611425061990_n-640x400.jpg",
        "deceased":  False,
    },
    {
        "name":      "Tostaky",
        "breed":     "Chat",
        "species":   "chat",
        "nickname":  "Mini puce toujours grognon",
        "image_url": "https://actani.fr/wp-content/uploads/2022/08/0188-640x400.jpg",
        "deceased":  False,
    },
    {
        "name":      "Rousseau",
        "breed":     "Chat",
        "species":   "chat",
        "nickname":  "Chargé de la sécurité",
        "image_url": "https://actani.fr/wp-content/uploads/2020/06/DSC03842-640x400.jpg",
        "deceased":  True,
    },
    {
        "name":      "Kovou",
        "breed":     "Chat",
        "species":   "chat",
        "nickname":  "Chargé de communication",
        "image_url": "https://actani.fr/wp-content/uploads/2020/06/kovou_jeune-1-640x400.jpg",
        "deceased":  False,
    },
]

# armes thématiques pour les animaux
WEAPONS_DATA = [
    {"name": "Griffe acérée",     "damage": 35, "description": "Des griffes tranchantes comme des rasoirs."},
    {"name": "Morsure féroce",    "damage": 50, "description": "Une morsure puissante et implacable."},
    {"name": "Rugissement",       "damage": 20, "description": "Un cri qui paralyse l'adversaire de peur."},
    {"name": "Bâton magique",     "damage": 30, "description": "L'arme fétiche de Chopin redoutable !"},
    {"name": "Hurlement perçant", "damage": 40, "description": "La spécialité de Toundra à la moindre frustration."},
    {"name": "Regard de chat",    "damage": 25, "description": "Un regard fixe qui désarçonne n'importe quel ennemi."},
    {"name": "Poids écrasant",    "damage": 55, "description": "48 kg d'Echo fonçant sur l'adversaire bonne chance !"},
]

print("Création des armes...")
weapons = []
for w in WEAPONS_DATA:
    weapon, created = Weapon.objects.get_or_create(name=w['name'], defaults=w)
    weapons.append(weapon)
    print(f"   {'[NEW]' if created else '[OK]'} {weapon.name} ({weapon.damage} dmg)")

# on associe chaque animal à son arme
WEAPON_MAP = {
    "Shana":   "Griffe acérée",
    "Chopin":  "Bâton magique",
    "Toundra": "Hurlement perçant",
    "Echo":    "Poids écrasant",
    "Tostaky": "Regard de chat",
    "Rousseau":"Griffe acérée",
    "Kovou":   "Regard de chat",
}

# dresseur1 : les chiens, dresseur2 : les chats
USERS_SETUP = [
    {
        "username":    "dresseur1",
        "password":    "motdepass123",
        "army_name":   "La Meute d'ACT'ani",
        "army_desc":   "Les chiens de Morgane sont bien éduqués, bienveillants, et redoutables au combat !",
        "animal_names": ["Shana", "Chopin", "Toundra", "Echo"],
    },
    {
        "username":    "dresseur2",
        "password":    "motdepass123",
        "army_name":   "Les Félins d'ACT'ani",
        "army_desc":   "Les chats de Morgane sont discrets, rusés, et maîtres de la maison !",
        "animal_names": ["Tostaky", "Rousseau", "Kovou"],
    },
]

# on indexe les animaux par nom pour y accéder plus facilement
animals_by_name = {a["name"]: a for a in ACTANI_ANIMALS}
weapons_by_name = {w.name: w for w in weapons}

print("\nCréation des utilisateurs et de leurs armées...")
for setup in USERS_SETUP:
    # création ou récupération de l'utilisateur
    user, u_created = User.objects.get_or_create(username=setup['username'])
    user.set_password(setup['password'])
    user.save()
    print(f"\n   {'[NEW]' if u_created else '[OK]'} Utilisateur : {setup['username']}")

    # création de l'armée associée
    army, a_created = Army.objects.get_or_create(
        owner=user,
        defaults={
            'name':        setup['army_name'],
            'description': setup['army_desc'],
        }
    )
    print(f"   Armée : {army.name} ({'créée' if a_created else 'existante'})")

    # ajout des animaux dans l'armée
    for animal_name in setup['animal_names']:
        animal_data = animals_by_name.get(animal_name)
        if not animal_data:
            continue

        weapon_name = WEAPON_MAP.get(animal_name)
        weapon      = weapons_by_name.get(weapon_name)

        animal, created = Animal.objects.get_or_create(
            name=animal_data['name'],
            army=army,
            defaults={
                'breed':     animal_data['breed'],
                'image_url': animal_data['image_url'],
                'weapon':    weapon,
            }
        )
        statut = "(décédé)" if animal_data['deceased'] else "en vie"
        print(f"   {'[NEW]' if created else '[OK]'} {animal.name} ({animal_data['species']}) — {animal_data['nickname']} [{statut}]")

print("\nPeuplement terminé ! Données issues de : https://actani.fr")
print("\nIdentifiants des comptes de test :")
print("  dresseur1 /motdepass123")
print("  dresseur2 /motdepass123")
