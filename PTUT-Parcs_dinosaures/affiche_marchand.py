import pygame
import pygame_setup

marchand = pygame.image.load("MARCHAND.PNG")
marchand_pos = pygame.Vector2(400, 20)
marchand_radius_x = 92
marchand_radius_y = 74

def affiche(x, y):
    '''
    Fonction prenant deux arguments :
    x -> objet position pygame ; y -> objet position pygame
    Cette fonction, est appelée à chaque passage dans la boucle dans le programme principal.
    Elle affiche le personnage aux coordonnées x et y.
    '''
    pygame_setup.screen.blit(marchand, (int(x), int(y)))