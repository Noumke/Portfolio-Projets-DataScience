import pygame
import pygame_setup
import capital as cap
import dinosaures as d
import salles as s


def affiche(current_room):
    '''
    Fonction prenant un argument :
    current_room -> dict
    La fonction sera exécutée à chaque passage dans la boucle du programme principal.
    Elle affiche les rectangles blancs sur le fond de la salle.
    '''
    for rec in current_room["chemins"] :
        pygame.draw.rect(pygame_setup.screen, "white", (rec["x"], rec["y"], rec["lo"], rec["la"]))
    for din in current_room["dinosaures"]:
        if din["existe"]:
            if din["faim"] <= 200 and din["santé"] <= 200:
                pygame_setup.screen.blit(pygame.image.load(din["element"]), din["image"])
            else:
                if pygame_setup.var == round(din["prix"] / 2):
                    pygame_setup.var = False
                pygame.draw.rect(pygame_setup.screen, "gray", (din["image"][0], din["image"][1], din["ray_x"], din["ray_y"]))
