# Pokeon — Pokédex Web

Application web permettant de consulter des informations sur les Pokémons via l'API [PokeAPI](https://pokeapi.co).
Projet réalisé dans le cadre du cours de développement web (2ème année).

---

## Fonctionnalités

- **Recherche** : trouver un Pokémon par son numéro (nom, types, stats, image, cri audio)
- **Liste** : parcourir tous les Pokémons avec filtre par génération (Gen I à IX)
- **Baies** : consulter la liste des 64 baies avec image, description et caractéristiques
- **Comparateur** : comparer les statistiques de deux Pokémons côte à côte

---

## Utilisation

Aucune installation nécessaire. Il suffit d'ouvrir le fichier dans le navigateur :

```
Pokeon/pokemon.html
```

Une connexion internet est requise pour appeler l'API PokeAPI.

---

## Structure

```
Pokeon/
├── pokemon.html   # interface utilisateur + styles CSS
└── pokemon.js     # logique : appels API, rendu, interactions
```

---

## API utilisée

[PokeAPI](https://pokeapi.co) — API publique et gratuite sur l'univers Pokémon.

Endpoints utilisés :
- `GET /pokemon/{id}` — données du Pokémon
- `GET /pokemon-species/{id}` — description de l'espèce
- `GET /pokemon?limit=...&offset=...` — liste paginée
- `GET /berry?limit=64` — liste des baies
- `GET /item/{id}` — détails et image d'une baie

---

## Auteurs

Ndiaye & Touré — BUT Informatique, Université Clermont Auvergne
