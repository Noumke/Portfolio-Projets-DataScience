import pygame
import pygame_setup
# On défnit l'image du personnage, ses coordonnées x et y, sa longueur, sa largeur.
player = pygame.image.load("Personnage.jpg")
player_pos = pygame.Vector2(410, 260)
player_radius_x = 31
player_radius_y = 42

def affiche(x, y):
    '''
    Fonction prenant deux arguments :
    x -> objet position pygame ; y -> objet position pygame
    Cette fonction, est appelée à chaque passage dans la boucle dans le programme principal.
    Elle affiche le personnage aux coordonnées x et y.
    '''
    pygame_setup.screen.blit(player, (int(x), int(y)))