"""
Parametres globaux de la simulation ACO

Ce fichier contient
les dimensions de la grille
les positions du nid et de la nourriture
les parametres de l algorithme ACO
la definition des obstacles
la definition des zones difficiles
"""

# Dimensions de la grille
NB_LIGNES = 30
NB_COLONNES = 30
TAILLE_CASE = 20


# Positions importantes
POSITION_NID = (1, 2)
POSITION_NOURRITURE = (22, 22)


# Parametres ACO
NB_FOURMIS = 150

EVAPORATION_PHEROMONE = 0.08
QUANTITE_PHEROMONE = 50

ALPHA = 1.5
BETA = 4.0

NOMBRE_ITERATIONS_EXPLORATION = 800
NOMBRE_IMAGES_PAR_SECONDE = 30


# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
GRIS = (220, 220, 220)
GRIS_GRILLE = (200, 200, 200)

COULEUR_OBSTACLE = (0, 0, 0)
COULEUR_ZONE_DIFFICILE = (200, 50, 50)


# Obstacles
OBSTACLES = {

    # Trait vertical haut
    (3, 18), (4, 18), (5, 18),

    # Point noir centre droit
    (12, 22),

    # Trait vertical milieu
    (14, 13), (15, 13), (16, 13),

    # Point noir bas gauche
    (18, 6),

    # Trait vertical bas
    (22, 12), (23, 12),

    # Trait horizontal droite
    (14, 26), (14, 27), (14, 28),

    # Bloc pres de la nourriture
    (25, 25), (25, 26),
    (26, 25)
}


# Zones difficiles
ZONES_DIFFICILES = {

    # Zone gauche haute
    (6, 2), (6, 3), (6, 4),

    # Zone gauche basse
    (16, 2), (16, 3),

    # Zone centrale
    (7, 14), (7, 15),

    # Zone milieu bas
    (17, 14), (17, 15), (17, 16)
}

COUT_ZONE_DIFFICILE = 3
