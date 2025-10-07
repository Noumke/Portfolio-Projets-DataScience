import salles as room
import pygame_setup
import pygame

pygame.init()
capital = 0
font = pygame.font.Font(None, 20)

def augmente_capital(capital):
    for k in room.alter[1:]:
        for i in k["dinosaures"]:
            if i["existe"]:
                capital += i["capital"]
    return capital

def affiche_capital(capital):
    text_surface = font.render(str(capital), True, "black")
    pygame_setup.screen.blit(text_surface, (825, 21))
    

