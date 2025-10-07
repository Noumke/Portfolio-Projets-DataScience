import pygame
# Définiion de l'écran dans un module à part, pour que les modules qui l'utilisent n'aient pas
# à importer le programme principal.
screen = pygame.display.set_mode((900, 600))
vit_perso = 3
var = True
lx1 = 110
ly1 = 110

lx2 = 650
ly2 = 110

lx3 = 110
ly3 = 140

lx4 = 650
ly4 = 140

lx5 = 400
ly5 = 170

l = [(lx1, ly1), (lx2, ly2), (lx3, ly3), (lx4, ly4), (lx5, ly5)]