import chemins as c
import dinosaures as din


def create_room(cs, dinosaurs):
    '''
    Fonction prenant deux arguments :
    cs -> list of dicts ; dinosaurs -> list of dicts
    Elle retourne un dictionnaire :
        clés : "chemins", "dinosaures"
        valeurs : cs, dinosaurs

    Ex : room_a = create_room(liste_chemins, liste_dinosaures)
    >>> room_a
    {"chemins" : liste_chemins, "dinosaures" : liste_dinosaures}
    '''
    return {"chemins" : cs, "dinosaures" : dinosaurs}

room_1 = create_room(c.l1, din.ld1)
room_2 = create_room(c.l2, din.ld2)
room_3 = create_room(c.l3, din.ld3)
room_4 = create_room(c.l4, din.ld4)
room_5 = create_room(c.l5, din.ld5)
room_6 = create_room(c.l6, din.ld6)
room_7 = create_room(c.l7, din.ld7)
room_8 = create_room(c.l8, din.ld8)
room_9 = create_room(c.l9, din.ld9)
room_10 = create_room(c.l10, din.ld10)
room_11 = create_room(c.l11, din.ld11)
room_12 = create_room(c.l12, din.ld12)
room_13 = create_room(c.l13, din.ld13)
room_14 = create_room(c.l14, din.ld14)
room_15 = create_room(c.l15, din.ld15)
room_16 = create_room(c.l16, din.ld16)
room_17 = create_room(c.l17, din.ld17)
room_18 = create_room(c.l18, din.ld18)
room_19 = create_room(c.l19, din.ld19)
room_20 = create_room(c.l20, din.ld20)

alter = [1, room_1, room_2, room_3, room_4, room_5, room_6, room_7, room_8, room_9, room_10, room_11, room_12, room_13, room_14, room_15, room_16, room_17, room_18, room_19, room_20]

architecture = {
    1 : {"gauche" : room_2, "bas" : room_3},
    2 : {"haut" : room_5, "droite" : room_1},
    3 : {"haut" : room_1, "bas" : room_7, "gauche" : room_6, "droite" : room_8},
    4 : {"bas" : room_8, "droite" : room_9},
    5 : {"droite" : room_10, "bas" : room_2},
    6 : {"droite" : room_3},
    7 : {"haut" : room_3, "bas" : room_12, "gauche" : room_11, "droite" : room_13},
    8 : {"haut" : room_4, "gauche" : room_3},
    9 : {"gauche" : room_4, "bas" : room_14},
    10 : {"gauche" : room_5, "droite" : room_15},
    11 : {"droite" : room_7},
    12 : {"haut" : room_7},
    13 : {"gauche" : room_7},
    14 : {"haut" : room_9, "bas" : room_16},
    15 : {"haut" : room_17, "gauche" : room_10, "droite" : room_18},
    16 : {"haut" : room_14},
    17 : {"gauche" : room_19, "bas" : room_15, "droite" : room_20},
    18 : {"gauche" : room_15},
    19 : {"droite" : room_17},
    20 : {"gauche" : room_17}}