# ⚔️ Guerre des Animaux — API Django REST

## Identifiants de test
| Utilisateur | Mot de passe |
|-------------|--------------|
| dresseur1   | password123  |
| dresseur2   | password123  |

---

## Installation et lancement

```bash
# 1. Installer les dépendances
pip install -r requirements.txt

# 2. Créer la base de données
python manage.py migrate

# 3. Peupler avec les données scrappées depuis Dog CEO API
python scripts/populate_db.py

# 4. Lancer le serveur Django
python manage.py runserver

# 5. Ouvrir le client web
# Ouvrir client/index.html dans votre navigateur
```

---

## Endpoints de l'API

### Authentification
| Méthode | URL               | Description              | Auth |
|---------|-------------------|--------------------------|------|
| POST    | /api/auth/login/  | Connexion → retourne token | Non |
| POST    | /api/auth/logout/ | Déconnexion               | Oui  |

### Mon armée (authentifié)
| Méthode | URL                        | Description                  |
|---------|----------------------------|------------------------------|
| GET     | /api/my-army/              | Voir mon armée               |
| POST    | /api/my-army/              | Créer mon armée              |
| PUT     | /api/my-army/              | Modifier mon armée           |
| GET     | /api/my-army/animals/      | Lister mes animaux           |
| POST    | /api/my-army/animals/      | Ajouter un animal            |
| DELETE  | /api/my-army/animals/{id}/ | Supprimer un animal          |

### Arme d'un animal (propriétaire uniquement)
| Méthode | URL                         | Description              |
|---------|-----------------------------|--------------------------|
| POST    | /api/animals/{id}/weapon/   | Assigner/créer une arme  |
| DELETE  | /api/animals/{id}/weapon/   | Retirer l'arme           |

### Vues publiques (sans authentification)
| Méthode | URL            | Description            |
|---------|----------------|------------------------|
| GET     | /api/armies/   | Toutes les armées      |
| GET     | /api/animals/  | Tous les animaux       |
| GET     | /api/weapons/  | Toutes les armes       |
| POST    | /api/weapons/  | Créer une arme (auth)  |

---

## Structure du projet
```
guerre_animaux/
├── manage.py
├── requirements.txt
├── README.md
├── guerre_animaux/
│   ├── settings.py
│   └── urls.py
├── api/
│   ├── models.py       ← Army, Animal, Weapon
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── scripts/
│   └── populate_db.py  ← Scrape Dog CEO API
└── client/
    └── index.html      ← Interface web
```
