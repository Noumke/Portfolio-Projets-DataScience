import pygame
from time import *
import temps
import menu_courant as cumenu
import textes as t
import menus as m
import dinosaures as din

def change_sante():
    '''
    Fonction ne prenant pas d'argument.
    Elle change continuellement la faim des dinosaures.
    '''
    for dino in din.ld1:
        dino["santé"] = dino["santé"] + 0.2

def soin(dino):
    '''
    Fonction prenant un argument.
    dino -> dict
    Cette fonction donne un repas à un dinosaure. Sa faim diminue de 3.
    '''
    sleep(0.5)
    
    if dino["santé"] >= 10800:
        dino["santé"] -= 10800
    else:
        dino["santé"] = 0

def teste_soin():
    keys = pygame.key.get_pressed()
    if cumenu.current_menu == m.menu_6 and keys[pygame.K_RETURN] and m.menu_5["selection"] == t.text_53:
        calin(din.dico_dinosaures_textes[cumenu.current_menu["selection"]["texte"]]) 
