import pygame
import dinosaures as din
import menu_courant as cumenu
import salle_courante as curoom
import menus as m
from time import *
import salles as s
import chemins as c
import perso_affiche as charprint
import capital as cap

def teste_ajoute():
    keys = pygame.key.get_pressed()
    if cumenu.current_menu == m.menu_9 and keys[pygame.K_RETURN]:
        for k in din.liste_dinos_2:
            if din.corresp_dinos[k["element"]] == cumenu.current_menu["selection"]["texte"]:
                if din.dino21 == k and din.dino21["prix"] <= cap.capital:
                    din.dino21 = din.create_dinosaur((int(din.dino21_pos.x), int(din.dino21_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld2 = [din.dino21, din.dino22]
                    s.room_2 = s.create_room(c.l2, din.ld2)
                    curoom.current_room = s.room_2
                    cap.capital -= din.dino21["prix"]
                if din.dino22 == k and din.dino22["prix"] <= cap.capital:
                    din.dino22 = din.create_dinosaur((int(din.dino22_pos.x), int(din.dino22_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld2 = [din.dino21, din.dino22]
                    s.room_2 = s.create_room(c.l2, din.ld2)
                    curoom.current_room = s.room_2
                    cap.capital -= din.dino22["prix"]
                if din.dino31 == k and din.dino31["prix"] <= cap.capital:
                    din.dino31 = din.create_dinosaur((int(din.dino31_pos.x), int(din.dino31_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld3 = [din.dino31, din.dino32, din.dino33, din.dino34, din.dino35]
                    s.room_3 = s.create_room(c.l3, din.ld3)
                    curoom.current_room = s.room_3
                    cap.capital -= din.dino31["prix"]
                if din.dino32 == k and din.dino32["prix"] <= cap.capital:
                    din.dino32 = din.create_dinosaur((int(din.dino32_pos.x), int(din.dino32_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld3 = [din.dino31, din.dino32, din.dino33, din.dino34, din.dino35]
                    s.room_3 = s.create_room(c.l3, din.ld3)
                    curoom.current_room = s.room_3
                    cap.capital -= din.dino32["prix"]

                if din.dino33 == k and din.dino33["prix"] <= cap.capital:
                    din.dino33 = din.create_dinosaur((int(din.dino33_pos.x), int(din.dino33_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld3 = [din.dino31, din.dino32, din.dino33, din.dino34, din.dino35]
                    s.room_3 = s.create_room(c.l3, din.ld3)
                    curoom.current_room = s.room_3
                    cap.capital -= din.dino33["prix"]
                if din.dino34 == k and din.dino34["prix"] <= cap.capital:
                    din.dino34 = din.create_dinosaur((int(din.dino34_pos.x), int(din.dino34_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld3 = [din.dino31, din.dino32, din.dino33, din.dino34, din.dino35]
                    s.room_3 = s.create_room(c.l3, din.ld3)
                    curoom.current_room = s.room_3
                    cap.capital -= din.dino34["prix"]
                if din.dino35 == k and din.dino35["prix"] <= cap.capital:
                    din.dino35 = din.create_dinosaur((int(din.dino34_pos.x), int(din.dino34_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld3 = [din.dino31, din.dino32, din.dino33, din.dino34, din.dino35]
                    s.room_3 = s.create_room(c.l3, din.ld3)
                    curoom.current_room = s.room_3
                    cap.capital -= din.dino35["prix"]
                if din.dino41 == k and din.dino41["prix"] <= cap.capital:
                    din.dino41 = din.create_dinosaur((int(din.dino41_pos.x), int(din.dino41_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", True)
                    din.ld4 = [din.dino41, din.dino42]
                    s.room_4 = s.create_room(c.l4, din.ld4)
                    curoom.current_room = s.room_4
                    cap.capital -= din.dino41["prix"]
                if din.dino42 == k and din.dino42["prix"] <= cap.capital:
                    din.dino42 = din.create_dinosaur((int(din.dino42_pos.x), int(din.dino42_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld4 = [din.dino41, din.dino42]
                    s.room_4 = s.create_room(c.l4, din.ld4)
                    curoom.current_room = s.room_4
                    cap.capital -= din.dino42["prix"]
                if din.dino51 == k and din.dino51["prix"] <= cap.capital:
                    din.dino51 = din.create_dinosaur((int(din.dino51_pos.x), int(din.dino51_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld5 = [din.dino51, din.dino52]
                    s.room_5 = s.create_room(c.l5, din.ld5)
                    curoom.current_room = s.room_5
                    cap.capital -= din.dino51["prix"]
                if din.dino52 == k and din.dino52["prix"] <= cap.capital:
                    din.dino52 = din.create_dinosaur((int(din.dino52_pos.x), int(din.dino52_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld5 = [din.dino51, din.dino52]
                    s.room_5 = s.create_room(c.l5, din.ld5)
                    curoom.current_room = s.room_5
                    cap.capital -= din.dino52["prix"]
                if din.dino61 == k and din.dino61["prix"] <= cap.capital:
                    din.dino61 = din.create_dinosaur((int(din.dino61_pos.x), int(din.dino61_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", True)
                    din.ld6 = [din.dino61]
                    s.room_6 = s.create_room(c.l6, din.ld6)
                    curoom.current_room = s.room_6
                    cap.capital -= din.dino61["prix"]
                if din.dino71 == k and din.dino71["prix"] <= cap.capital:
                    din.dino71 = din.create_dinosaur((int(din.dino71_pos.x), int(din.dino71_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld7 = [din.dino71, din.dino72, din.dino73, din.dino74]
                    s.room_7 = s.create_room(c.l7, din.ld7)
                    curoom.current_room = s.room_7
                    cap.capital -= din.dino71["prix"]
                if din.dino72 == k and din.dino72["prix"] <= cap.capital:
                    din.dino72 = din.create_dinosaur((int(din.dino72_pos.x), int(din.dino72_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld7 = [din.dino71, din.dino72, din.dino73, din.dino74] 
                    s.room_7 = s.create_room(c.l7, din.ld7)
                    curoom.current_room = s.room_7
                    cap.capital -= din.dino72["prix"]
                if din.dino73 == k and din.dino73["prix"] <= cap.capital:
                    din.dino73 = din.create_dinosaur((int(din.dino73_pos.x), int(din.dino73_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld7 = [din.dino71, din.dino72, din.dino73, din.dino74]
                    s.room_7 = s.create_room(c.l7, din.ld7)
                    curoom.current_room = s.room_7
                    cap.capital -= din.dino73["prix"]
                if din.dino74 == k and din.dino74["prix"] <= cap.capital:
                    din.dino74 = din.create_dinosaur((int(din.dino74_pos.x), int(din.dino74_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
                    din.ld7 = [din.dino71, din.dino72, din.dino73, din.dino74]  
                    s.room_7 = s.create_room(c.l7, din.ld7)
                    curoom.current_room = s.room_7
                    cap.capital -= din.dino74["prix"]
                if din.dino81 == k and din.dino81["prix"] <= cap.capital:
                    din.dino81 = din.create_dinosaur((int(din.dino81_pos.x), int(din.dino81_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld8 = [din.dino81, din.dino82]
                    s.room_8 = s.create_room(c.l8, din.ld8)
                    curoom.current_room = s.room_8
                    cap.capital -= din.dino81["prix"]
                if din.dino82 == k and din.dino82["prix"] <= cap.capital:
                    din.dino82 = din.create_dinosaur((int(din.dino82_pos.x), int(din.dino82_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", True)
                    din.ld8 = [din.dino81, din.dino82]
                    s.room_8 = s.create_room(c.l8, din.ld8)
                    curoom.current_room = s.room_8
                    cap.capital -= din.dino82["prix"]
                if din.dino91 == k and din.dino91["prix"] <= cap.capital:
                    din.dino91 = din.create_dinosaur((int(din.dino91_pos.x), int(din.dino91_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", True)
                    din.ld9 = [din.dino91, din.dino92]
                    s.room_9 = s.create_room(c.l9, din.ld9)
                    curoom.current_room = s.room_9
                    cap.capital -= din.dino91["prix"]
                if din.dino92 == k and din.dino92["prix"] <= cap.capital:
                    din.dino92 = din.create_dinosaur((int(din.dino92_pos.x), int(din.dino92_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld9 = [din.dino91, din.dino92]
                    s.room_9 = s.create_room(c.l9, din.ld9)
                    curoom.current_room = s.room_9
                    cap.capital -= din.dino92["prix"]
                if din.dino101 == k and din.dino101["prix"] <= cap.capital:
                    din.dino101 = din.create_dinosaur((int(din.dino101_pos.x), int(din.dino101_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld10 = [din.dino101, din.dino102, din.dino103]
                    s.room_10 = s.create_room(c.l10, din.ld10)
                    curoom.current_room = s.room_10
                    cap.capital -= din.dino101["prix"]
                if din.dino102 == k and din.dino102["prix"] <= cap.capital:
                    din.dino102 = din.create_dinosaur((int(din.dino102_pos.x), int(din.dino102_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld10 = [din.dino101, din.dino102, din.dino103]
                    s.room_10 = s.create_room(c.l10, din.ld10)
                    curoom.current_room = s.room_10
                    cap.capital -= din.dino102["prix"]
                if din.dino103 == k and din.dino103["prix"] <= cap.capital:
                    din.dino103 = din.create_dinosaur((int(din.dino103_pos.x), int(din.dino103_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld10 = [din.dino101, din.dino102, din.dino103]
                    s.room_10 = s.create_room(c.l10, din.ld10)
                    curoom.current_room = s.room_10
                    cap.capital -= din.dino103["prix"]
                if din.dino111 == k and din.dino111["prix"] <= cap.capital:
                    din.dino111 = din.create_dinosaur((int(din.dino111_pos.x), int(din.dino111_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", True)
                    din.ld11 = [din.dino111]
                    s.room_11 = s.create_room(c.l11, din.ld11)
                    curoom.current_room = s.room_11
                    cap.capital -= din.dino111["prix"]
                if din.dino121 == k and din.dino121["prix"] <= cap.capital:
                    din.dino121 = din.create_dinosaur((int(din.dino121_pos.x), int(din.dino121_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", True)
                    din.ld12 = [din.dino121]
                    s.room_12 = s.create_room(c.l12, din.ld12)
                    curoom.current_room = s.room_12
                    cap.capital -= din.dino111["prix"]
                if din.dino131 == k and din.dino131["prix"] <= cap.capital:
                    din.dino131 = din.create_dinosaur((int(din.dino131_pos.x), int(din.dino131_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", True)
                    din.ld13 = [din.dino131]
                    s.room_13 = s.create_room(c.l13, din.ld13)
                    curoom.current_room = s.room_13
                    cap.capital -= din.dino131["prix"]
                if din.dino141 == k and din.dino141["prix"] <= cap.capital:
                    din.dino141 = din.create_dinosaur((int(din.dino141_pos.x), int(din.dino141_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", True)
                    din.ld14 = [din.dino141, din.dino142]
                    s.room_14 = s.create_room(c.l14, din.ld14)
                    curoom.current_room = s.room_14
                    cap.capital -= din.dino141["prix"]
                if din.dino142 == k and din.dino142["prix"] <= cap.capital:
                    din.dino142 = din.create_dinosaur((int(din.dino142_pos.x), int(din.dino142_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", True)
                    din.ld14 = [din.dino141, din.dino142]
                    s.room_14 = s.create_room(c.l14, din.ld14)
                    curoom.current_room = s.room_14
                    cap.capital -= din.dino142["prix"]
                if din.dino151 == k and din.dino151["prix"] <= cap.capital:
                    din.dino151 = din.create_dinosaur((int(din.dino151_pos.x), int(din.dino151_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld15 = [din.dino151, din.dino152, din.dino153, din.dino154]
                    s.room_15 = s.create_room(c.l15, din.ld15)
                    curoom.current_room = s.room_15
                    cap.capital -= din.dino151["prix"]
                if din.dino152 == k and din.dino152["prix"] <= cap.capital:
                    din.dino152 = din.create_dinosaur((int(din.dino152_pos.x), int(din.dino152_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld15 = [din.dino151, din.dino152, din.dino153, din.dino154] 
                    s.room_15 = s.create_room(c.l15, din.ld15)
                    curoom.current_room = s.room_15
                    cap.capital -= din.dino152["prix"]
                if din.dino153 == k and din.dino153["prix"] <= cap.capital:
                    din.dino153 = din.create_dinosaur((int(din.dino153_pos.x), int(din.dino153_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld15 = [din.dino151, din.dino152, din.dino153, din.dino154]
                    s.room_15 = s.create_room(c.l15, din.ld15)
                    curoom.current_room = s.room_15
                    cap.capital -= din.din153["prix"]
                if din.dino154 == k and din.dino154["prix"] <= cap.capital:
                    din.dino154 = din.create_dinosaur((int(din.dino154_pos.x), int(din.dino154_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld15 = [din.dino151, din.dino152, din.dino153, din.dino154]
                    s.room_15 = s.create_room(c.l15, din.ld15)
                    curoom.current_room = s.room_15
                    cap.capital -= din.dino154["prix"]
                if din.dino161 == k and din.dino161["prix"] <= cap.capital:
                    din.dino161 = din.create_dinosaur((int(din.dino161_pos.x), int(din.dino161_pos.y)), 20, 20, 70, 10000, 1, 1, 1, 1, 999, "Roi_dinosaure.png", True)
                    din.ld16 = [din.dino161]
                    s.room_16 = s.create_room(c.l16, din.ld16)
                    curoom.current_room = s.room_16
                    cap.capital -= din.dino161["prix"]
                if din.dino171 == k and din.dino171["prix"] <= cap.capital:
                    din.dino171 = din.create_dinosaur((int(din.dino171_pos.x), int(din.dino171_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld17 = [din.dino171, din.dino172, din.dino173, din.dino174]
                    s.room_17 = s.create_room(c.l17, din.ld17)
                    curoom.current_room = s.room_17
                    cap.capital -= din.dino171["prix"]
                if din.dino172 == k and din.dino172["prix"] <= cap.capital:
                    din.dino172 = din.create_dinosaur((int(din.dino172_pos.x), int(din.dino172_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld17 = [din.dino171, din.dino172, din.dino173, din.dino174]
                    s.room_17 = s.create_room(c.l17, din.ld17)
                    curoom.current_room = s.room_17
                    cap.capital -= din.dino172["prix"]
                if din.dino173 == k and din.dino173["prix"] <= cap.capital:
                    din.dino173 = din.create_dinosaur((int(din.dino173_pos.x), int(din.dino173_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", True)
                    din.ld17 = [din.dino171, din.dino172, din.dino173, din.dino174]
                    s.room_17 = s.create_room(c.l17, din.ld17)
                    curoom.current_room = s.room_17
                    cap.capital -= din.dino173["prix"]
                if din.dino174 == k and din.dino174["prix"] <= cap.capital:
                    din.dino174 = din.create_dinosaur((int(din.dino174_pos.x), int(din.dino174_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
                    din.ld17 = [din.dino171, din.dino172, din.dino173, din.dino174]
                    s.room_17 = s.create_room(c.l17, din.ld17)
                    curoom.current_room = s.room_17
                    cap.capital -= din.dino174["prix"]
                if din.dino181 == k and din.dino181["prix"] <= cap.capital:
                    din.dino181 = din.create_dinosaur((int(din.dino181_pos.x), int(din.dino181_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Normal_adulte.png", True)
                    din.ld18 = [din.dino181]
                    s.room_18 = s.create_room(c.l18, din.ld18)
                    curoom.current_room = s.room_18
                    cap.capital -= din.dino181["prix"]
                if din.dino191 == k and din.dino191["prix"] <= cap.capital:
                    din.dino191 = din.create_dinosaur((int(din.dino191_pos.x), int(din.dino191_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Normal_adulte.png", True)
                    din.ld19 = [din.dino191]
                    s.room_19 = s.create_room(c.l19, din.ld19)
                    curoom.current_room = s.room_19
                    cap.capital -= din.dino191["prix"]
                if din.dino201 == k and din.dino201["prix"] <= cap.capital:   
                    din.dino201 = din.create_dinosaur((int(din.dino201_pos.x), int(din.dino201_pos.y)), 20, 20, 50, 1000, 1, 1, 1, 1, 999, "Abyssal.png", True)
                    din.ld20 = [din.dino201]
                    s.room_20 = s.create_room(c.l20, din.ld20)
                    curoom.current_room = s.room_20
                    cap.capital -= din.dino201["prix"]
                s.architecture = {
                1 : {"gauche" : s.room_2, "bas" : s.room_3},
                2 : {"haut" : s.room_5, "droite" : s.room_1},
                3 : {"haut" : s.room_1, "bas" : s.room_7, "gauche" : s.room_6, "droite" : s.room_8},
                4 : {"bas" : s.room_8, "droite" : s.room_9},
                5 : {"droite" : s.room_10, "bas" : s.room_2},
                6 : {"droite" : s.room_3},
                7 : {"haut" : s.room_3, "bas" : s.room_12, "gauche" : s.room_11, "droite" : s.room_13},
                8 : {"haut" : s.room_4, "gauche" : s.room_3},
                9 : {"gauche" : s.room_4, "bas" : s.room_14},
                10 : {"gauche" : s.room_5, "droite" : s.room_15},
                11 : {"droite" : s.room_7},
                12 : {"haut" : s.room_7},
                13 : {"gauche" : s.room_7},
                14 : {"haut" : s.room_9, "bas" : s.room_16},
                15 : {"haut" : s.room_17, "gauche" : s.room_10, "droite" : s.room_18},
                16 : {"haut" : s.room_14},
                17 : {"gauche" : s.room_19, "bas" : s.room_15, "droite" : s.room_20},
                18 : {"gauche" : s.room_15},
                19 : {"droite" : s.room_17},
                20 : {"gauche" : s.room_17}}
                s.alter = [1, s.room_1, s.room_2, s.room_3, s.room_4, s.room_5, s.room_6, s.room_7, s.room_8, s.room_9, s.room_10, s.room_11, s.room_12, s.room_13, s.room_14, s.room_15, s.room_16, s.room_17, s.room_18, s.room_19, s.room_20]
                
                charprint.player_pos = pygame.Vector2(450, 250)

                break
            sleep(0.5)




