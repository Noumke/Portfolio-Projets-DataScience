"""
Affichage de la simulation ACO

Ce module gere uniquement le rendu graphique
grille obstacles zones difficiles pheromones chemin nid nourriture fourmis et noms
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
    COULEUR_ZONE_DIFFICILE
)

# Association coordonnees vers libelles visibles
NOMS_LIEUX = {
    (1, 2): "Salle 9",
    (4, 17): "Escalier 1",
    (10, 18): "Escalier 2",
    (16, 12): "Escalier 3",
    (11, 5): "Escalier chemin 2",
    POSITION_NOURRITURE: "R U"
}


def coord_case_vers_ecran(x, y):
    """
    Convertit une coordonnee de case en coin haut gauche en pixels
    """
    return y * TAILLE_CASE, x * TAILLE_CASE


def centre_case_vers_ecran(x, y):
    """
    Convertit une coordonnee de case en centre en pixels
    """
    px, py = coord_case_vers_ecran(x, y)
    return px + TAILLE_CASE // 2, py + TAILLE_CASE // 2


def dessiner_grille(ecran):
    """
    Dessine la grille de fond
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            px, py = coord_case_vers_ecran(i, j)
            rect = pygame.Rect(px, py, TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(ecran, GRIS_GRILLE, rect, 1)


def dessiner_pheromones(ecran, grille_pheromones):
    """
    Dessine les pheromones avec une intensite proportionnelle
    """
    for i in range(NB_LIGNES):
        for j in range(NB_COLONNES):
            valeur = grille_pheromones[i][j]
            if valeur <= 0.01:
                continue

            intensite = min(255, int(valeur * 0.7))
            couleur = (0, 0, intensite)

            px, py = coord_case_vers_ecran(i, j)
            rect = pygame.Rect(px, py, TAILLE_CASE, TAILLE_CASE)
            pygame.draw.rect(ecran, couleur, rect)


def dessiner_zones_difficiles(ecran):
    """
    Dessine les zones difficiles
    """
    for x, y in ZONES_DIFFICILES:
        px, py = coord_case_vers_ecran(x, y)
        rect = pygame.Rect(px, py, TAILLE_CASE, TAILLE_CASE)
        pygame.draw.rect(ecran, COULEUR_ZONE_DIFFICILE, rect)


def dessiner_obstacles(ecran):
    """
    Dessine les obstacles
    """
    for x, y in OBSTACLES:
        px, py = coord_case_vers_ecran(x, y)
        rect = pygame.Rect(px, py, TAILLE_CASE, TAILLE_CASE)
        pygame.draw.rect(ecran, BLANC, rect)


def dessiner_chemin_optimal(ecran, chemin):
    """
    Dessine le chemin optimal sous forme de points
    """
    # Points jaunes discrets pour visualiser le meilleur chemin
    for x, y in chemin:
        cx, cy = centre_case_vers_ecran(x, y)
        pygame.draw.circle(ecran, (255, 255, 0), (cx, cy), 4)


def dessiner_nid_nourriture(ecran):
    """
    Dessine le nid et la nourriture
    """
    x, y = POSITION_NID
    px, py = coord_case_vers_ecran(x, y)
    pygame.draw.rect(ecran, ROUGE, (px, py, TAILLE_CASE, TAILLE_CASE))

    x, y = POSITION_NOURRITURE
    px, py = coord_case_vers_ecran(x, y)
    pygame.draw.rect(ecran, VERT, (px, py, TAILLE_CASE, TAILLE_CASE))


def dessiner_fourmis(ecran, fourmis):
    """
    Dessine les fourmis sous forme de petits points
    """
    for fourmi in fourmis:
        x, y = fourmi.position
        cx, cy = centre_case_vers_ecran(x, y)
        pygame.draw.circle(ecran, NOIR, (cx, cy), 3)


def dessiner_noms_lieux(ecran, police):
    """
    Affiche les libelles sur les cases importantes
    """
    for (x, y), texte in NOMS_LIEUX.items():
        surface = police.render(texte, True, NOIR)
        px, py = coord_case_vers_ecran(x, y)
        ecran.blit(surface, (px, py - 18))


def afficher(ecran, grille_pheromones, fourmis, chemin_optimal):
    """
    Rend une image complete de la simulation
    """
    ecran.fill(BLANC)

    dessiner_pheromones(ecran, grille_pheromones)
    dessiner_zones_difficiles(ecran)
    dessiner_obstacles(ecran)
    dessiner_grille(ecran)
    dessiner_chemin_optimal(ecran, chemin_optimal)
    dessiner_nid_nourriture(ecran)
    dessiner_fourmis(ecran, fourmis)

    # Police simple pour les libelles
    police = pygame.font.SysFont(None, 18)
    dessiner_noms_lieux(ecran, police)

    pygame.display.flip()
