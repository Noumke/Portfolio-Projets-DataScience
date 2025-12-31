"""
Gestion de l affichage de la simulation ACO

Ce fichier affiche
la grille
les obstacles
les zones difficiles
les pheromones avec intensite visible
le chemin optimal
le nid
la nourriture
les fourmis
"""

import pygame

from parametres import (
    NB_LIGNES,
    NB_COLONNES,
    TAILLE_CASE,
    POSITION_NID,
    POSITION_NOURRITURE,
    OBSTACLES,
    ZONES_DIFFICILES,
    BLANC,
    NOIR,
    ROUGE,
    VERT,
    GRIS_GRILLE,
    COULEUR_OBSTACLE,
    COULEUR_ZONE_DIFFICILE
)


def dessiner_grille(ecran):
    """
    Dessine la grille
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            rect = pygame.Rect(
                j * TAILLE_CASE,
                i * TAILLE_CASE,
                TAILLE_CASE,
                TAILLE_CASE
            )
            pygame.draw.rect(ecran, GRIS_GRILLE, rect, 1)


def dessiner_pheromones(ecran, grille_pheromones):
    """
    Dessine les pheromones avec une intensite proportionnelle
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            valeur = grille_pheromones[i][j]

            if valeur > 0.01:
                intensite = min(255, int(valeur * 0.7))
                couleur = (0, 0, intensite)

                rect = pygame.Rect(
                    j * TAILLE_CASE,
                    i * TAILLE_CASE,
                    TAILLE_CASE,
                    TAILLE_CASE
                )

                pygame.draw.rect(ecran, couleur, rect)


def dessiner_zones_difficiles(ecran):
    """
    Dessine les zones difficiles
    """
    for x, y in ZONES_DIFFICILES:
        rect = pygame.Rect(
            y * TAILLE_CASE,
            x * TAILLE_CASE,
            TAILLE_CASE,
            TAILLE_CASE
        )
        pygame.draw.rect(ecran, COULEUR_ZONE_DIFFICILE, rect)


def dessiner_obstacles(ecran):
    """
    Dessine les obstacles
    """
    for x, y in OBSTACLES:
        rect = pygame.Rect(
            y * TAILLE_CASE,
            x * TAILLE_CASE,
            TAILLE_CASE,
            TAILLE_CASE
        )
        pygame.draw.rect(ecran, COULEUR_OBSTACLE, rect)


def dessiner_chemin_optimal(ecran, chemin):
    """
    Dessine le chemin optimal
    """
    for x, y in chemin:
        cx = y * TAILLE_CASE + TAILLE_CASE // 2
        cy = x * TAILLE_CASE + TAILLE_CASE // 2
        pygame.draw.circle(
            ecran,
            (255, 255, 0),
            (cx, cy),
            4
        )


def dessiner_nid_nourriture(ecran):
    """
    Dessine le nid et la nourriture
    """
    x, y = POSITION_NID
    pygame.draw.rect(
        ecran,
        ROUGE,
        (y * TAILLE_CASE, x * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
    )

    x, y = POSITION_NOURRITURE
    pygame.draw.rect(
        ecran,
        VERT,
        (y * TAILLE_CASE, x * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE)
    )


def dessiner_fourmis(ecran, fourmis):
    """
    Dessine les fourmis de facon discrete
    """
    for fourmi in fourmis:
        x, y = fourmi.position
        cx = y * TAILLE_CASE + TAILLE_CASE // 2
        cy = x * TAILLE_CASE + TAILLE_CASE // 2
        pygame.draw.circle(
            ecran,
            NOIR,
            (cx, cy),
            3
        )


def afficher(ecran, grille_pheromones, fourmis, chemin_optimal):
    """
    Fonction principale d affichage
    """
    ecran.fill(BLANC)

    dessiner_pheromones(ecran, grille_pheromones)
    dessiner_zones_difficiles(ecran)
    dessiner_obstacles(ecran)
    dessiner_grille(ecran)
    dessiner_chemin_optimal(ecran, chemin_optimal)
    dessiner_nid_nourriture(ecran)
    dessiner_fourmis(ecran, fourmis)

    pygame.display.flip()
