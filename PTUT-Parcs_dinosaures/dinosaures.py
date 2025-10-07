# Prochaine étape
import pygame
import temps


def create_dinosaur(img, radius_x, radius_y, capital, prix, faim, fatigue, niv_activité, santé, love_for_player, element, existe):
    '''
    Fonction prenant plusieurs arguments :
    img -> son image, ou, dans la version beta, ses coordonnées x et y. (str / tuple)
    radius_x et radius_y -> ses dimensions (int)
    faim -> int ; santé -> int ; love_for_player -> int
    niv_activité -> int ; element -> str
    Cette fonction créé un dictionnaire ayant pour clés dans l'ordre les éléments entrés en argument, 
    et ayant pour valeurs ce que contiennent ces arguments.
    '''
    return {"image" : img, "ray_x" : radius_x, "ray_y" : radius_y, "capital" : capital, "prix" : prix, "faim" : faim, "fatigue" : fatigue, "niv_activité" : niv_activité, "santé" : santé, "affection" : love_for_player, "element" : element, "existe" : existe}

# Création des dinosaures de la version beta
dino11_pos = pygame.Vector2(100, 50)
dino11 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
dino12_pos = pygame.Vector2(700, 200)
dino12 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
dino13_pos = pygame.Vector2(20, 370)
dino13 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", True)
dino14_pos = pygame.Vector2(330,430)
dino14 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", True)
ld1 = [dino11, dino12, dino13, dino14]

dino21_pos = pygame.Vector2(700, 100)
dino21 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino22_pos = pygame.Vector2(100, 300)
dino22 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
ld2 = [dino21, dino22]

dino31_pos = pygame.Vector2(0, 0)
dino31 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
dino32_pos = pygame.Vector2(300, 0)
dino32 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
dino33_pos = pygame.Vector2(700, 100)
dino33 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
dino34_pos = pygame.Vector2(200,300)
dino34 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
dino35_pos = pygame.Vector2(700,400)
dino35 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
ld3 = [dino31, dino32, dino33, dino34, dino35]

dino41_pos = pygame.Vector2(100, 100)
dino41 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", False)
dino42_pos = pygame.Vector2(700, 400)
dino42 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
ld4 = [dino41, dino42]

dino51_pos = pygame.Vector2(100, 100)
dino51 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
dino52_pos = pygame.Vector2(700, 400)
dino52 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
ld5 = [dino51, dino52]

dino61_pos = pygame.Vector2(100, 300)
dino61 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", False)
ld6 = [dino61]

dino71_pos = pygame.Vector2(100, 100)
dino71 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
dino72_pos = pygame.Vector2(700, 100)
dino72 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
dino73_pos = pygame.Vector2(100, 300)
dino73 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
dino74_pos = pygame.Vector2(700,300)
dino74 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Rouge_enfant.png", False)
ld7 = [dino71, dino72, dino73, dino74]

dino81_pos = pygame.Vector2(100, 100)
dino81 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
dino82_pos = pygame.Vector2(600, 300)
dino82 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", False)
ld8 = [dino81, dino82]

dino91_pos = pygame.Vector2(100, 300)
dino91 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", False)
dino92_pos = pygame.Vector2(600, 100)
dino92 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
ld9 = [dino91, dino92]

dino101_pos = pygame.Vector2(100, 100)
dino101 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino102_pos = pygame.Vector2(600, 200)
dino102 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino103_pos = pygame.Vector2(100, 300)
dino103 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
ld10 = [dino101, dino102, dino103]

dino111_pos = pygame.Vector2(100, 300)
dino111 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", False)
ld11 = [dino111]

dino121_pos = pygame.Vector2(400, 300)
dino121 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", False)
ld12 = [dino121]

dino131_pos = pygame.Vector2(300, 100)
dino131 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 10, 100, 1, 1, 1, 1, 999, "Lave_enfant.png", False)
ld13 = [dino131]

dino141_pos = pygame.Vector2(100, 200)
dino141 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 5, 60, 1, 1, 1, 1, 999, "Rouge_ado.png", False)
dino142_pos = pygame.Vector2(700, 200)
dino142 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Lave_adulte.png", False)
ld14 = [dino141, dino142]

dino151_pos = pygame.Vector2(100, 100)
dino151 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
dino152_pos = pygame.Vector2(600, 100)
dino152 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino153_pos = pygame.Vector2(200, 100)
dino153 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
dino154_pos = pygame.Vector2(600, 300)
dino154 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
ld15 = [dino151, dino152, dino153, dino154]

dino161_pos = pygame.Vector2(400, 300)
dino161 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 70, 10000, 1, 1, 1, 1, 999, "Roi-dinosaure.png", False)
ld16 = [dino161]

dino171_pos = pygame.Vector2(100, 100)
dino171 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
dino172_pos = pygame.Vector2(700, 200)
dino172 = create_dinosaur((int(dino12_pos.x), int(dino12_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino173_pos = pygame.Vector2(100, 400)
dino173 = create_dinosaur((int(dino13_pos.x), int(dino13_pos.y)), 20, 20, 2, 50, 1, 1, 1, 1, 999, "Normal_ado.png", False)
dino174_pos = pygame.Vector2(700,400)
dino174 = create_dinosaur((int(dino14_pos.x), int(dino14_pos.y)), 20, 20, 1, 10, 1, 1, 1, 1, 999, "Normal_enfant.png", False)
ld17 = [dino171, dino172, dino173, dino174]

dino181_pos = pygame.Vector2(300, 100)
dino181 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Normal_adulte.png", False)
ld18 = [dino181]

dino191_pos = pygame.Vector2(100, 300)
dino191 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 15, 500, 1, 1, 1, 1, 999, "Normal_adulte.png", False)
ld19 = [dino191]

dino201_pos = pygame.Vector2(700, 200)
dino201 = create_dinosaur((int(dino11_pos.x), int(dino11_pos.y)), 20, 20, 50, 1000, 1, 1, 1, 1, 999, "Abyssal.png", False)
ld20 = [dino201]

ll_dinos = [ld1, ld2, ld3, ld4, ld5, ld6, ld7, ld8, ld9, ld10, ld11, ld12, ld13, ld14, ld15, ld16, ld17, ld18, ld19, ld20]
liste_dinos = ld1 + ld2 + ld3 + ld4 + ld5 + ld6 + ld7 + ld8 + ld9 + ld10 + ld11 + ld12 + ld13 + ld14 + ld15 + ld16 + ld17 + ld18 + ld19 + ld20
liste_dinos_2 = ld2 + ld3 + ld4 + ld5 + ld6 + ld7 + ld8 + ld9 + ld10 + ld11 + ld12 + ld13 + ld14 + ld15 + ld16 + ld17 + ld18 + ld19 + ld20
corresp_dinos = {"Normal_enfant.png" : "Normalosaure (10 P)",
"Normal_ado.png" : "Normalosaure évolué (50 P)",
"Normal_adulte.png" : "Normalosaure titanesque (500 P)",
"Rouge_enfant.png" : "Redosaure (10 P)",
"Rouge_ado.png" : "Redosaure évolué (60 P)",
"Rouge_adulte.png" : "Redosaure titanesque (90 P)",
"Lave_enfant.png" : "Lavasaure (100 P)",
"Lave_adulte.png" : "Lavasaure titanesque (500 P)",
"Abyssal.png" : "Serpent-dinosaure Abyssal (1000 P)",
"Roi-dinosaure.png" : "Roid-dinosaure (10000 P)"
}

dico_dinosaures_textes = {"dino11" : dino11,
"dino12" : dino12,
"dino13" : dino13,
"dino14" : dino14,
"dino21" : dino21,
"dino22" : dino22,
"dino31" : dino31,
"dino32" : dino32,
"dino33" : dino33,
"dino34" : dino34,
"dino41" : dino41,
"dino42" : dino42,
"dino51" : dino51,
"dino52" : dino52,
"dino61" : dino61,
"dino71" : dino71,
"dino72" : dino72,
"dino73" : dino73,
"dino74" : dino74,
"dino81" : dino81,
"dino82" : dino82,
"dino91" : dino91,
"dino92" : dino92,
"dino101" : dino101,
"dino102" : dino102,
"dino103" : dino103,
"dino111" : dino111,
"dino121" : dino121,
"dino131" : dino131,
"dino141" : dino141,
"dino142" : dino142,
"dino151" : dino151,
"dino152" : dino152,
"dino153" : dino153,
"dino154" : dino154,
"dino161" : dino161,
"dino171" : dino171,
"dino172" : dino172,
"dino173" : dino173,
"dino174" : dino174,
"dino181" : dino181,
"dino191" : dino191,
"dino201" : dino201}






