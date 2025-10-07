import pygame
import menus as m
import pygame_setup
import dinosaures as d
import gere_faim
import gere_sante
import gere_affection
import salle_courante as curoom

pygame.init()
font = pygame.font.Font(None, 20)


def gere(current_menu):
    if current_menu == m.menu_13 :
        long = len(curoom.current_room["dinosaures"])
        liste = pygame_setup.l[:long + 1]
        for k in range(long):
            if curoom.current_room["dinosaures"][k]["existe"] :
                text_surface = font.render(d.corresp_dinos[curoom.current_room["dinosaures"][k]["element"]] + " : " + str(round(curoom.current_room["dinosaures"][k]["faim"] / 60)), True, "black")
                pygame_setup.screen.blit(text_surface, liste[k])
    if current_menu == m.menu_14 :
        long = len(curoom.current_room["dinosaures"])
        liste = pygame_setup.l[:long + 1]
        for k in range(long):
            if curoom.current_room["dinosaures"][k]["existe"] :
                text_surface = font.render(d.corresp_dinos[curoom.current_room["dinosaures"][k]["element"]] + " : " + str(round(curoom.current_room["dinosaures"][k]["santé"] / 60)), True, "black")
                pygame_setup.screen.blit(text_surface, liste[k])
    if current_menu == m.menu_15 :
        long = len(curoom.current_room["dinosaures"])
        liste = pygame_setup.l[:long + 1]
        for k in range(long):
            if curoom.current_room["dinosaures"][k]["existe"] :
                text_surface = font.render(d.corresp_dinos[curoom.current_room["dinosaures"][k]["element"]] + " : " + str(round(curoom.current_room["dinosaures"][k]["affection"] / 60)), True, "black")
                pygame_setup.screen.blit(text_surface, liste[k])






