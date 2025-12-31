"""
Comportement d une fourmi pour la simulation ACO

Ce module definit le comportement individuel d une fourmi
exploration retour depot de pheromones et choix probabiliste
"""

import random
import math

from parametres import (
    NB_LIGNES,
    NB_COLONNES,
    POSITION_NID,
    POSITION_NOURRITURE,
    OBSTACLES,
    ALPHA,
    BETA,
    QUANTITE_PHEROMONE,
    NOMBRE_ITERATIONS_EXPLORATION,
    cout_case
)

from pheromones import deposer_pheromone


class Fourmi:
    """
    Modele une fourmi individuelle
    """

    def __init__(self):
        """
        Initialise l etat de la fourmi
        """
        self.position = POSITION_NID
        self.chemin_aller = [POSITION_NID]
        self.en_retour = False
        self.index_retour = 0

    def obtenir_voisins(self):
        """
        Retourne les voisins accessibles depuis la position courante
        """
        x, y = self.position
        voisins = []

        directions = [(1, 0), (~0, 0), (0, 1), (0, ~0)]

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < NB_LIGNES and 0 <= ny < NB_COLONNES:
                if (nx, ny) not in OBSTACLES:
                    voisins.append((nx, ny))

        # Evite le demi tour immediat pendant l exploration
        if len(self.chemin_aller) >= 2 and not self.en_retour:
            precedente = self.chemin_aller[-2]
            if precedente in voisins and len(voisins) > 1:
                voisins.remove(precedente)

        return voisins

    def avancer_exploration(self, voisins):
        """
        Deplacement exploratoire base sur la distance et le cout
        """
        scores = []

        for v in voisins:
            distance = math.dist(v, POSITION_NOURRITURE)
            cout = cout_case(v)
            score = 1.0 / ((distance + 1.0) * cout)
            scores.append(score)

        nouvelle_position = random.choices(voisins, weights=scores, k=1)[0]

        self.position = nouvelle_position
        self.chemin_aller.append(nouvelle_position)

        # Passage en phase retour si la nourriture est atteinte
        if self.position == POSITION_NOURRITURE:
            self.en_retour = True
            self.index_retour = len(self.chemin_aller) - 1

    def avancer_probabiliste(self, voisins, grille_pheromones):
        """
        Deplacement probabiliste base sur pheromones et heuristique
        """
        probabilites = []

        for x, y in voisins:
            tau = grille_pheromones[x][y] + 0.0001
            distance = math.dist((x, y), POSITION_NOURRITURE) + 0.0001
            cout = cout_case((x, y))

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
            self.en_retour = True
            self.index_retour = len(self.chemin_aller) - 1

    def avancer_retour(self, grille_pheromones):
        """
        Retour vers le nid avec depot progressif de pheromones
        """
        if self.index_retour <= 0:
            self.reinitialiser()
            return

        longueur = len(self.chemin_aller)
        if longueur <= 1:
            self.reinitialiser()
            return

        delta = QUANTITE_PHEROMONE / float(longueur)

        position_retour = self.chemin_aller[self.index_retour]
        deposer_pheromone(grille_pheromones, position_retour, delta)

        self.index_retour = self.index_retour + (~0)
        self.position = self.chemin_aller[self.index_retour]

    def avancer(self, grille_pheromones, iteration):
        """
        Met a jour la fourmi pour une iteration
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
        Replace la fourmi au nid
        """
        self.position = POSITION_NID
        self.chemin_aller = [POSITION_NID]
        self.en_retour = False
        self.index_retour = 0
