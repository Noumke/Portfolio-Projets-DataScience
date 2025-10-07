import pygame
import pygame_setup
import menus as m
import textes as t
import salles as s
import salle_courante as curoom
import perso_affiche as charprint
from time import *
import capital as cap
import sys
import pause


# On définit le menu courant, comme les salles.
current_menu = m.menu_0

def test_chgt_menu(current_menu):
    '''
    Fonction prenant un argument :
    current_menu -> dict
    Elle teste :
        - Si on appuie sur M, on entre dans le menu principal.
        - Si on appuie sur A, on entre dans le menu des actions disponibles.
        - Si on appuie sur BACKSPACE, on retourne au menu précédent.
        - Si on appuie sur RETURN (Entree), on entre dans le menu sélectionné.
        - Si on appuie sur UP ou DOWN, on change la sélection du menu.
    Elle retourne également le menu courant qui sort de la fonction en fonction de tous les tests.
    '''
    attendre = 0.1
    keys = pygame.key.get_pressed()
    if current_menu == m.menu_0 and keys[pygame.K_m]:
        current_menu = m.menu_1
    
    if current_menu == m.menu_0 and keys[pygame.K_a]:
        current_menu = m.menu_5

    if current_menu == m.menu_0 and keys[pygame.K_e]:
        current_menu = m.menu_12


    
    if current_menu != m.menu_0 and keys[pygame.K_BACKSPACE]:
        if current_menu == m.menu_1 :
            current_menu = m.menu_0
            sleep(attendre)
        elif current_menu == m.menu_6 :
            current_menu = m.menu_5
            sleep(attendre)
        elif current_menu == m.menu_2 or current_menu == m.menu_3 or current_menu == m.menu_4:
            current_menu = m.menu_1
            sleep(attendre)
        elif current_menu == m.menu_5 or current_menu == m.menu_7 or current_menu == m.menu_12:
            current_menu = m.menu_0
        elif current_menu == m.menu_8:
            current_menu = m.menu_7
            sleep(attendre)
        elif current_menu == m.menu_9 or current_menu == m.menu_10 or current_menu == m.menu_11:
            current_menu = m.menu_8
            sleep(attendre)
        elif current_menu == m.menu_13 or current_menu == m.menu_14 or current_menu == m.menu_15:
            current_menu = m.menu_12
            sleep(attendre)

    if keys[pygame.K_RETURN]:
        if current_menu["selection"] == t.text_11:
            pause.pause()
        if current_menu["selection"] == t.text_12 :
            current_menu = m.menu_2
            sleep(attendre)
        if current_menu["selection"] == t.text_13 :
            pygame.quit()
            sys.exit()
        elif current_menu["selection"] == t.text_14 :
            current_menu = m.menu_3
            sleep(attendre)
        elif current_menu["selection"] == t.text_15 :
            current_menu = m.menu_4
            sleep(attendre)
        elif current_menu["selection"] == t.text_81 :
            current_menu = m.menu_9
            sleep(attendre)
        elif current_menu["selection"] == t.text_82 :
            current_menu = m.menu_10
            sleep(attendre)
        elif current_menu["selection"] == t.text_83 :
            current_menu = m.menu_11
            sleep(attendre)
        elif current_menu["selection"] == t.text_121 :
            current_menu = m.menu_13
        elif current_menu["selection"] == t.text_122 :
            current_menu = m.menu_14
        elif current_menu["selection"] == t.text_123 :
            current_menu = m.menu_15
        elif current_menu["selection"] == t.text_101:
            if cap.capital >= 500:
                pygame_setup.vit_perso += 1
                cap.capital -= 500
        elif current_menu == m.menu_5:
            current_menu = m.menu_6
            sleep(attendre)
        elif current_menu == m.menu_7:
            current_menu = m.menu_8
            sleep(attendre)
        



    if current_menu != m.menu_0 and keys[pygame.K_UP] and current_menu["selection"] != current_menu["liste_textes"][0]:
        
        current_menu["selection"]["couleur"] = "black"
        current_menu["liste_textes"][current_menu["liste_textes"].index(current_menu["selection"])-1]["couleur"] = "red"
        current_menu["selection"] = current_menu["liste_textes"][current_menu["liste_textes"].index(current_menu["selection"])-1]
        sleep(attendre)
    
    if current_menu != m.menu_0 and keys[pygame.K_DOWN] and current_menu["selection"] != current_menu["liste_textes"][-1]:
        current_menu["liste_textes"][current_menu["liste_textes"].index(current_menu["selection"])+1]["couleur"] = "red"
        current_menu["selection"]["couleur"] = "black"
        current_menu["selection"] = current_menu["liste_textes"][current_menu["liste_textes"].index(current_menu["selection"])+1]
        sleep(attendre)

    if 400 < charprint.player_pos.x < 492 and 94 < charprint.player_pos.y < 144 and current_menu == m.menu_0 and keys[pygame.K_RETURN] and curoom.current_room == s.room_1:
        current_menu = m.menu_7
        sleep(attendre)

        
    

    return current_menu

