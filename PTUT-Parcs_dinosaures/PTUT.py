import pygame
import capital as cap
import textes as t
import deplacement as move
import perso_affiche as charprint
import affiche_marchand as marprint
import pygame_setup
import temps


import chemins as c
import dinosaures as d
import ajoute_dinosaure as add_din
import gere_faim as faim
import gere_affection as affection
import gere_sante as sante

import salles as s
import salles_affiche as roomprint
import salle_courante as curoom

import menus as m
import menus_affiche as menuprint
import menu_courant as cumenu
import menu_capital as capmenu



# Setup Pygame
pygame.init()
clock = pygame.time.Clock()
running = True

while running:
    temps.horloge += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Fond de l'écran
    pygame_setup.screen.fill("green")

    # Affichage de la salle
    add_din.teste_ajoute()
    curoom.current_room = curoom.test_chgt_salle(curoom.current_room)
    roomprint.affiche(curoom.current_room)

    # Affichage du personnage
    charprint.affiche(charprint.player_pos.x, charprint.player_pos.y)
    if curoom.current_room == s.room_1:
        marprint.affiche(marprint.marchand_pos.x, marprint.marchand_pos.y)
    if cumenu.current_menu == m.menu_0:
        move.change_xy_perso()

    # Affichage du menu
    cumenu.current_menu = cumenu.test_chgt_menu(cumenu.current_menu)
    
    menuprint.affiche(cumenu.current_menu)
    capmenu.gere(cumenu.current_menu)
    # Faim des dosaures
    faim.change_faim()
    affection.change_affection()
    faim.teste_repas()
    affection.teste_calin()
    sante.teste_soin()
    sante.change_sante()
    if temps.horloge % 600 == 0:
        cap.capital = cap.augmente_capital(cap.capital)
    cap.affiche_capital(cap.capital)
    
    

    # Setup pygame
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()