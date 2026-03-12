"""
Boucle principale de la simulation ACO

Ce fichier
initialise la simulation
gere la boucle principale
coordonne les fourmis
met a jour les pheromones
affiche letat courant
"""

import pygame

from parametres import (
    NB_LIGNES,
    NB_COLONNES,
    TAILLE_CASE,
    NB_FOURMIS,
    NOMBRE_IMAGES_PAR_SECONDE
)

from fourmi import Fourmi
from pheromones import (
    creer_grille_pheromones,
    evaporer_pheromones,
    meilleur_chemin
)

from affichage import afficher


def lancer_simulation():
    """
    Lance la simulation ACO
    """
    pygame.init()

    largeur = NB_COLONNES * TAILLE_CASE
    hauteur = NB_LIGNES * TAILLE_CASE

    ecran = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Simulation A C O")

    horloge = pygame.time.Clock()

    grille_pheromones = creer_grille_pheromones()
    fourmis = [Fourmi() for _ in range(NB_FOURMIS)]

    iteration = 0
    en_cours = True

    while en_cours:

        horloge.tick(NOMBRE_IMAGES_PAR_SECONDE)
        iteration += 1

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

        # Evaporation des pheromones
        evaporer_pheromones(grille_pheromones)

        # Deplacement des fourmis
        for fourmi in fourmis:
            fourmi.avancer(grille_pheromones, iteration)

        # Calcul du chemin optimal pour affichage
        chemin_optimal = meilleur_chemin(grille_pheromones)

        # Affichage
        afficher(
            ecran,
            grille_pheromones,
            fourmis,
            chemin_optimal
        )

    pygame.quit()


if __name__ == "__main__":
    lancer_simulation()
