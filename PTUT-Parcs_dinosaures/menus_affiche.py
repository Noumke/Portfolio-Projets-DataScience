import pygame
import pygame_setup
import menus as m
pygame.init()

pygame.display.set_caption("Gestion d'un Parc de Dinosaures")
font = pygame.font.Font(None, 20)


def affiche(current_menu):
    '''
    Fonction prenant un argument :
    current_menu -> dict
    Elle affiche le menu : son texte, et son fond d'écran.
    '''
    if current_menu != m.menu_0:
        pygame.draw.rect(pygame_setup.screen, current_menu["couleur"], (100, 100, 700, 400))
    for t in current_menu["liste_textes"]:
        text_surface = font.render(t["texte"], True, t["couleur"])
        pygame_setup.screen.blit(text_surface, (t["x"], t["y"]))
    
    
