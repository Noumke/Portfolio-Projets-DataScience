"""
Parametres globaux de la simulation ACO

Cas concret avec deux chemins possibles
Les escaliers sont modelises uniquement par des couts
"""

# Dimensions de la grille
NB_LIGNES = 30
NB_COLONNES = 30
TAILLE_CASE = 20


# Positions importantes
POSITION_NID = (1, 2)
POSITION_NOURRITURE = (22, 22)


# Parametres ACO
NB_FOURMIS = 300
EVAPORATION_PHEROMONE = 0.2
QUANTITE_PHEROMONE = 50
ALPHA = 3
BETA = 1.5
NOMBRE_ITERATIONS_EXPLORATION = 1000
NOMBRE_IMAGES_PAR_SECONDE = 30


# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
GRIS_GRILLE = (200, 200, 200)
COULEUR_ZONE_DIFFICILE = (200, 50, 50)


# Outils internes
NEG_UN = ~0


def _segment_vertical(x1, x2, y):
    """
    Construit un segment vertical entre deux abscisses
    """
    cases = []
    step = 1 if x1 <= x2 else NEG_UN
    x = x1

    while x != x2 + step:
        cases.append((x, y))
        x = x + step

    return cases


def _segment_horizontal(x, y1, y2):
    """
    Construit un segment horizontal entre deux ordonnees
    """
    cases = []
    step = 1 if y1 <= y2 else NEG_UN
    y = y1

    while y != y2 + step:
        cases.append((x, y))
        y = y + step

    return cases


def construire_chemin(points):
    """
    Construit un chemin continu a partir de points cles
    """
    chemin = [points[0]]

    for a, b in zip(points, points[1:]):
        x1, y1 = a
        x2, y2 = b

        if x1 != x2:
            chemin.extend(_segment_vertical(x1, x2, y1)[1:])

        if y1 != y2:
            chemin.extend(_segment_horizontal(x2, y1, y2)[1:])

    return chemin


# Escaliers
ESCALIER_GROS = (11, 5)

ESCALIER_1 = (4, 17)
ESCALIER_2 = (10, 18)

ESCALIER_FINAL = (16, 12)

ESCALIERS_PETITS = {
    ESCALIER_1,
    ESCALIER_2,
    ESCALIER_FINAL
}


# Definition des chemins
POINTS_CHEMIN_1 = [
    POSITION_NID,
    (1, 18),
    ESCALIER_1,
    (10, 18),
    ESCALIER_2,
    (16, 18),
    ESCALIER_FINAL,
    POSITION_NOURRITURE
]

POINTS_CHEMIN_2 = [
    POSITION_NID,
    (11, 2),
    ESCALIER_GROS,
    (11, 12),
    ESCALIER_FINAL,
    POSITION_NOURRITURE
]


# Construction des chemins autorises
CHEMIN_1 = construire_chemin(POINTS_CHEMIN_1)
CHEMIN_2 = construire_chemin(POINTS_CHEMIN_2)

CASES_AUTORISEES = set(CHEMIN_1) | set(CHEMIN_2)


# Cout des cases
COUT_PETIT_ESCALIER = 2
COUT_GROS_ESCALIER = 100

COUT_CASES = {}

for c in ESCALIERS_PETITS:
    COUT_CASES[c] = COUT_PETIT_ESCALIER

COUT_CASES[ESCALIER_GROS] = COUT_GROS_ESCALIER


def cout_case(case):
    """
    Retourne le cout associe a une case
    """
    return COUT_CASES.get(case, 1)


# Zones difficiles
ZONES_DIFFICILES = set(ESCALIERS_PETITS) | {ESCALIER_GROS}
COUT_ZONE_DIFFICILE = 3


# Obstacles
OBSTACLES = set()

for i in range(NB_LIGNES):
    for j in range(NB_COLONNES):
        if (i, j) not in CASES_AUTORISEES:
            OBSTACLES.add((i, j))
