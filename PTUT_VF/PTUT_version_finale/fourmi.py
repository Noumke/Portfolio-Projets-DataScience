"""
Comportement dune fourmi pour la simulation ACO

Regles
exploration au depart
choix probabiliste base sur pheromones et heuristique
retour strict par le chemin inverse
depot progressif de pheromones au retour
entree directe au nid si adjacent
respect des obstacles
penalisation des zones difficiles
"""

import random
import math

from parametres import (
    NB_LIGNES,
    NB_COLONNES,
    POSITION_NID,
    POSITION_NOURRITURE,
    OBSTACLES,
    ZONES_DIFFICILES,
    COUT_ZONE_DIFFICILE,
    ALPHA,
    BETA,
    QUANTITE_PHEROMONE,
    NOMBRE_ITERATIONS_EXPLORATION
)

from pheromones import deposer_pheromone


class Fourmi:
    """
    Objet fourmi
    """

    def __init__(self):
        """
        Etat initial de la fourmi
        """
        self.position = POSITION_NID
        self.chemin_aller = [POSITION_NID]

        self.a_trouve_nourriture = False
        self.en_retour = False
        self.index_retour = 0

    def cout_case(self, case):
        """
        Cout de deplacement dune case
        """
        if case in ZONES_DIFFICILES:
            return COUT_ZONE_DIFFICILE
        return 1

    def obtenir_voisins(self):
        """
        Retourne les voisins accessibles
        obstacles exclus
        """
        x, y = self.position
        voisins = []

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < NB_LIGNES and 0 <= ny < NB_COLONNES:
                if (nx, ny) not in OBSTACLES:
                    voisins.append((nx, ny))

        if len(self.chemin_aller) >= 2 and not self.en_retour:
            precedente = self.chemin_aller[-2]
            if precedente in voisins and len(voisins) > 1:
                voisins.remove(precedente)

        return voisins

    def avancer_exploration(self, voisins):
        """
        Deplacement exploratoire sans pheromones
        """
        scores = []

        for v in voisins:
            distance = math.dist(v, POSITION_NOURRITURE)
            cout = self.cout_case(v)
            score = 1.0 / ((distance + 1.0) * cout)
            scores.append(score)

        nouvelle_position = random.choices(voisins, weights=scores, k=1)[0]

        self.position = nouvelle_position
        self.chemin_aller.append(nouvelle_position)

        if self.position == POSITION_NOURRITURE:
            self.a_trouve_nourriture = True
            self.en_retour = True
            self.index_retour = len(self.chemin_aller) - 1

    def avancer_probabiliste(self, voisins, grille_pheromones):
        """
        Deplacement probabiliste base sur pheromones
        """
        probabilites = []

        for v in voisins:
            ligne, colonne = v

            tau = grille_pheromones[ligne][colonne] + 0.0001
            distance = math.dist(v, POSITION_NOURRITURE) + 0.0001
            cout = self.cout_case(v)

            valeur_pheromone = tau ** ALPHA
            valeur_distance = (1.0 / distance) ** BETA

            score = valeur_pheromone * valeur_distance / cout
            probabilites.append(score)

        total = sum(probabilites)
        probabilites = [p / total for p in probabilites]

        nouvelle_position = random.choices(voisins, weights=probabilites, k=1)[0]

        self.position = nouvelle_position
        self.chemin_aller.append(nouvelle_position)

        if self.position == POSITION_NOURRITURE:
            self.a_trouve_nourriture = True
            self.en_retour = True
            self.index_retour = len(self.chemin_aller) - 1

    def avancer_retour(self, grille_pheromones):
        """
        Retour vers le nid avec depot de pheromones
        """
        x, y = self.position
        xn, yn = POSITION_NID

        if abs(x - xn) + abs(y - yn) == 1:
            self.reinitialiser()
            return

        longueur = len(self.chemin_aller)
        if longueur <= 1:
            self.reinitialiser()
            return

        delta = QUANTITE_PHEROMONE / float(longueur)

        if self.index_retour > 0:
            position_retour = self.chemin_aller[self.index_retour]

            deposer_pheromone(grille_pheromones, position_retour, delta)

            self.index_retour -= 1
            self.position = self.chemin_aller[self.index_retour]
        else:
            self.reinitialiser()

    def avancer(self, grille_pheromones, iteration):
        """
        Mise a jour dune fourmi pour une iteration
        """
        if self.en_retour:
            self.avancer_retour(grille_pheromones)
            return

        voisins = self.obtenir_voisins()
        if not voisins:
            self.reinitialiser()
            return

        if iteration < NOMBRE_ITERATIONS_EXPLORATION:
            self.avancer_exploration(voisins)
        else:
            self.avancer_probabiliste(voisins, grille_pheromones)

    def reinitialiser(self):
        """
        Reinitialise la fourmi au nid
        """
        self.position = POSITION_NID
        self.chemin_aller = [POSITION_NID]
        self.a_trouve_nourriture = False
        self.en_retour = False
        self.index_retour = 0
