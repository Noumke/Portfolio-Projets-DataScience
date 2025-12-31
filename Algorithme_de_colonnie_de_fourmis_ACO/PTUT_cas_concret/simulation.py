"""
Boucle principale de la simulation ACO

Ce module initialise la simulation
gere la boucle principale
coordonne les fourmis
met a jour les pheromones
declenche l affichage
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
    Lance et execute la simulation ACO
    """
    pygame.init()

    # Dimensions de la fenetre
    largeur = NB_COLONNES * TAILLE_CASE
    hauteur = NB_LIGNES * TAILLE_CASE
    ecran = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption("Simulation A C O")

    # Gestion du temps
    horloge = pygame.time.Clock()

    # Initialisation des donnees
    grille_pheromones = creer_grille_pheromones()
    fourmis = [Fourmi() for _ in range(NB_FOURMIS)]

    iteration = 0
    en_cours = True

    while en_cours:

        # Controle du nombre d images par seconde
        horloge.tick(NOMBRE_IMAGES_PAR_SECONDE)
        iteration += 1

        # Gestion des evenements
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

        # Evaporation globale des pheromones
        evaporer_pheromones(grille_pheromones)

        # Deplacement de chaque fourmi
        for fourmi in fourmis:
            fourmi.avancer(grille_pheromones, iteration)

        # Calcul du meilleur chemin a partir des pheromones
        chemin_optimal = meilleur_chemin(grille_pheromones)

        # Affichage de l etat courant
        afficher(
            ecran,
            grille_pheromones,
            fourmis,
            chemin_optimal
        )

    pygame.quit()


if __name__ == "__main__":
    lancer_simulation()
