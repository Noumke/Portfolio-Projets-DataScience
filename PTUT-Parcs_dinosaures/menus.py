import textes as t


def create_menu(liste_textes, couleur, selection):
    '''
    Fonction prenant trois arguments :
    liste_textes -> list ; couleur -> str / (aaa, bbb, ccc) ; selection -> dict (texte)
    Elle retourne un dictionnaire ayant pour clés "liste_textes", "couleur", et "selection" et ayant pour valeurs :
    liste_textes, couleur, et selection.
    '''
    return {"liste_textes" : liste_textes, "couleur" : couleur, "selection" : selection}

# Création des menus
menu_0 = create_menu(t.t0, "white", t.text_01)
menu_1 = create_menu(t.t1, "orange", t.text_11)
menu_2 = create_menu(t.t2, "orange", t.text_21)
menu_3 = create_menu(t.t3, "orange", t.text_31)
menu_4 = create_menu(t.t4, "orange", t.text_41)
menu_5 = create_menu(t.t5, "orange", t.text_51)
menu_6 = create_menu(t.t6, "orange", t.text_61)
menu_7 = create_menu(t.t7, "orange", t.text_71)
menu_8 = create_menu(t.t8, "orange", t.text_81)
menu_9 = create_menu(t.t9, "orange", t.text_91)
menu_10 = create_menu(t.t10, "orange", t.text_101)
menu_11 = create_menu(t.t11, "orange", t.text_111)
menu_12 = create_menu(t.t12, "orange", t.text_121)
menu_13 = create_menu(t.t13, "orange", t.text_131)
menu_14 = create_menu(t.t14, "orange", t.text_141)
menu_15 = create_menu(t.t15, "orange", t.text_151)

# Création des dictionnaires alternatifs pour parer au problème des clés dictionnaires dans un dictionnaire
alter_menus = [menu_0, menu_1, menu_2, menu_3, menu_4, menu_5, menu_6, menu_7, menu_8, menu_9, menu_10, menu_11, menu_12, menu_13, menu_14, menu_15]
alter_textes = [t.text_01, t.text_02, t.text_03, t.text_04, t.text_05, t.text_11, t.text_12, t.text_13, t.text_14, t.text_15, t.text_21, t.text_22, t.text_23, t.text_31, t.text_32, t.text_33, t.text_34, t.text_35, t.text_41, t.text_51, t.text_52, t.text_53, t.text_61, t.text_62, t.text_63, t.text_64, t.text_71, t.text_72, t.text_81, t.text_82, t.text_83, t.text_91, t.text_92, t.text_93, t.text_94, t.text_95, t.text_96, t.text_97, t.text_98, t.text_99, t.text_910, t.text_101, t.text_102, t.text_103, t.text_104, t.text_105, t.text_111, t.text_121, t.text_122, t.text_123, t.text_131, t.text_141, t.text_151]
# Création du dictionnaire architecture
architecture = {
    0 : {0 : menu_1, 1 : menu_5},
    1 : {4 : menu_2, 6 : menu_3, 7 : menu_4},
    5 : {13 : menu_6, 14 : menu_6, 15 : menu_6, 16 : menu_6}}