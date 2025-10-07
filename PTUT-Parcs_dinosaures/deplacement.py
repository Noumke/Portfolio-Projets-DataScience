import pygame
import perso_affiche as charprint
import pygame_setup



def change_xy_perso():
    '''
    Fonction ne prenant aucun argument.
    Elle est utilisée dans le script PTUT.py, pour, à chaque passage dans la boucle, 
    vérifier si le personnage ne touche pas le vert.
    Si on appuie sur une touche et que la condition précédente est remplie, alors on fait change les coordonnées du personnage.
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z] and pygame_setup.screen.get_at((int(charprint.player_pos.x)-1, int(charprint.player_pos.y)-1)) != (0, 255, 0) :
        charprint.player_pos.y -= pygame_setup.vit_perso
    if keys[pygame.K_s] and pygame_setup.screen.get_at((int(charprint.player_pos.x), int(charprint.player_pos.y+charprint.player_radius_y))) != (0, 255, 0):
        charprint.player_pos.y += pygame_setup.vit_perso
    if keys[pygame.K_q] and pygame_setup.screen.get_at((int(charprint.player_pos.x)-1, int(charprint.player_pos.y)-1)) != (0, 255, 0):
        charprint.player_pos.x -= pygame_setup.vit_perso
    if keys[pygame.K_d] and pygame_setup.screen.get_at((int(charprint.player_pos.x + charprint.player_radius_x), int(charprint.player_pos.y))) != (0, 255, 0):
        charprint.player_pos.x += pygame_setup.vit_perso

