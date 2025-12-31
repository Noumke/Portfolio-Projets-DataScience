"""
Gestion des pheromones pour la simulation ACO

Principe
creation dune grille de pheromones
evaporation globale a chaque iteration
depot de pheromones au retour des fourmis
calcul du meilleur chemin pour affichage
"""

import math

from parametres import (
    NB_LIGNES,
    NB_COLONNES,
    POSITION_NID,
    POSITION_NOURRITURE,
    EVAPORATION_PHEROMONE,
    OBSTACLES,
    ZONES_DIFFICILES,
    COUT_ZONE_DIFFICILE
)


VALEUR_MAX_PHEROMONE = 500


def creer_grille_pheromones():
    """
    Cree une grille initiale de pheromones
    """
    grille = []
    for i in range(NB_LIGNES):
        ligne = []
        for j in range(NB_COLONNES):
            ligne.append(0.0)
        grille.append(ligne)
    return grille


def evaporer_pheromones(grille):
    """
    Evaporation globale des pheromones
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            grille[i][j] = grille[i][j] * (1.0 - EVAPORATION_PHEROMONE)
            if grille[i][j] < 0.0:
                grille[i][j] = 0.0


def deposer_pheromone(grille, position, quantite):
    """
    Depot de pheromone sur une case donnee
    Aucun depot sur les obstacles
    """
    if position in OBSTACLES:
        return

    x, y = position
    nouvelle_valeur = grille[x][y] + quantite

    if nouvelle_valeur > VALEUR_MAX_PHEROMONE:
        nouvelle_valeur = VALEUR_MAX_PHEROMONE

    grille[x][y] = nouvelle_valeur


def existe_pheromones(grille):
    """
    Indique sil existe au moins une pheromone
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            if grille[i][j] > 0.0:
                return True
    return False


def voisins_valides(position):
    """
    Voisins accessibles en evitant les obstacles
    """
    x, y = position
    voisins = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < NB_LIGNES and 0 <= ny < NB_COLONNES:
            if (nx, ny) not in OBSTACLES:
                voisins.append((nx, ny))

    return voisins


def cout_case(case):
    """
    Cout dune case pour le calcul du chemin optimal
    """
    if case in ZONES_DIFFICILES:
        return COUT_ZONE_DIFFICILE
    return 1


def meilleur_chemin(grille):
    """
    Construction du meilleur chemin base sur les pheromones
    Fonction utilisee uniquement pour l affichage
    """
    if not existe_pheromones(grille):
        return []

    chemin = [POSITION_NID]
    position = POSITION_NID
    visites = set()
    visites.add(position)

    limite = NB_LIGNES * NB_COLONNES

    while position != POSITION_NOURRITURE and len(chemin) < limite:
        voisins = voisins_valides(position)

        if not voisins:
            break

        meilleur = None
        meilleure_valeur = -1.0

        for v in voisins:
            if v in visites:
                continue

            valeur = grille[v[0]][v[1]]
            valeur = valeur / float(cout_case(v))

            if valeur > meilleure_valeur:
                meilleure_valeur = valeur
                meilleur = v

        if meilleur is None:
            break

        chemin.append(meilleur)
        position = meilleur
        visites.add(position)

    return chemin
