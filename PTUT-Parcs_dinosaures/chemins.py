def create_path(x, y, lo, la):
    '''
    Fonction prenant quatre arguments:
    x -> int ; y -> int ; lo -> int ; la -> int
    La fonction prend l'abscisse, l'ordonnée, la longueur, la largeur.
    Elle retourne un dictionnaire :
        clés -> "x", "y", "lo", "la"
        valeurs -> les paramètres respectivement rentrés en argument.

    Ex : path_ab = create_path(0, 0, 100, 100)
    >>> path_ab
    {"x" : 0, "y" : 0, "lo" : 100, "la" : 100}
    '''
    return {"x" : x, "y" : y, "lo" : lo, "la" : la}

# Création des chemins de la salle 1
path_11 = create_path(400, 0, 100, 250)
path_12 = create_path(0, 250, 600, 100)
path_13 = create_path(200, 300, 100, 300)
path_14 = create_path(500, 300, 100, 300)
l1 = [path_11, path_12, path_13, path_14]
# Création des chemins de la salle 2
path_21 = create_path(400, 0, 100, 350)
path_22 = create_path(500, 250, 400, 100)
l2 = [path_21, path_22]
# Création des chemins de la salle 3
path_31 = create_path(200, 0, 100, 250)
path_32 = create_path(500, 0, 100, 600)
path_33 = create_path(0, 250, 900, 100)
l3 = [path_31, path_32, path_33]
# Création des chemins de la salle 4
path_41 = create_path(400, 350, 100, 300)
path_42 = create_path(400, 250, 600, 100)
l4 = [path_41, path_42]
# Création des chemins de la salle 5
path_51 = create_path(400, 250, 500, 100)
path_52 = create_path(400, 350, 100, 250)
l5 = [path_51, path_52]
# Création des chemins de la salle 6
path_61 = create_path(400, 250, 500, 100)
l6 = [path_61]
# Création des chemins de la salle 7
path_71 = create_path(500, 0, 100, 600)
path_72 = create_path(0, 250, 900, 100)
l7 = [path_71, path_72]
# Création des chemins de la salle 8
path_81 = create_path(400, 0, 100, 350)
path_82 = create_path(0, 250, 400, 100)
l8 = [path_81, path_82]
# Création des chemins de la salle 9
path_91 = create_path(0, 250, 500, 100)
path_92 = create_path(400, 350, 100, 250)
l9 = [path_91, path_92]
# Création des chemins de la salle 10
path_101 = create_path(0, 250, 400, 100)
path_102 = create_path(300, 100, 100, 400)
path_103 = create_path(400, 100, 500, 100)
path_104 = create_path(400, 400, 500, 100)
l10 = [path_101, path_102, path_103, path_104]
# Création des chemins de la salle 11
path_111 = create_path(400, 250, 500, 101)
l11 = [path_111]
# Création des chemins de la salle 12
path_121 = create_path(500, 0, 100, 300)
l12 = [path_121]
# Création des chemins de la salle 13
path_131 = create_path(0, 250, 500, 100)
l13 = [path_131]
# Création des chemins de la salle 14
path_141 = create_path(400, 0, 100, 600)
l14 = [path_141]
# Création des chemins de la salle 15
path_151 = create_path(400, 0, 100, 500)
path_152 = create_path(0, 100, 400, 100)
path_153 = create_path(500, 250, 400, 100)
path_154 = create_path(0, 400, 400, 100)
l15 = [path_151, path_152, path_153, path_154]
# Création des chemins de la salle 16
path_161 = create_path(400, 0, 100, 300)
l16 = [path_161]
# Création des chemins de la salle 17
path_171 = create_path(400, 100, 500, 100)
path_172 = create_path(400, 200, 100, 400)
path_173 = create_path(0, 250, 400, 100)
path_174 = create_path(500, 400, 400, 100)
l17 = [path_171, path_172, path_173, path_174]
# Création des chemins de la salle 18
path_181 = create_path(0, 250, 500, 101)
l18 = [path_181]
# Création des chemins de la salle 19
path_191 = create_path(400, 250, 500, 102)
l19 = [path_191]
# Création des chemins de la salle 20
path_201 = create_path(0, 100, 500, 100)
path_202 = create_path(0, 250, 500, 100)
path_203 = create_path(0, 400, 500, 100)
l20 = [path_201, path_202, path_203]
