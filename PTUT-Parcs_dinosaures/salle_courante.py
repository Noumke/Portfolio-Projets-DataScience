import salles as s
import perso_affiche as charprint

# Définition de la première salle courante. 
# La salle courante est la salle dans laquelle se situe le personnage.
current_room = s.room_1


def test_chgt_salle(current_room):
    '''
    Fonction prenant un argument :
    current_room -> dict
    current_room, dans le programme principal, doit être la salle courante appelée current_room.
    La fonction vérifie si le personnage se situe sur un bord de la salle.
    Si oui, elle change de salle en fonction de l'architecture de salles.py, 
    et en fonction du bord sur lequel se situe le personnage.
    '''


    if int(charprint.player_pos.x) <= 10 :
        a = s.architecture[s.alter.index(current_room)]["gauche"]        
        charprint.player_pos.x += 700
        current_room = a

    if int(charprint.player_pos.x) >= 900-charprint.player_radius_x :
        a = s.architecture[s.alter.index(current_room)]["droite"]
        charprint.player_pos.x-= 700
        current_room = a

    if int(charprint.player_pos.y) <= 10 :
        a = s.architecture[s.alter.index(current_room)]["haut"]
        charprint.player_pos.y += 500
        current_room = a

    if int(charprint.player_pos.y) >= 600-charprint.player_radius_y :
        a = s.architecture[s.alter.index(current_room)]["bas"]
        charprint.player_pos.y -= 400
        current_room = a
    return current_room