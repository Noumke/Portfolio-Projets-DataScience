import capital as cap

def create_text(texte, x, y, couleur):
    return {"texte" : texte, "x" : x, "y" : y, "couleur" : couleur}



text_01 = create_text("Menu (M)", 10, 20, "black")
text_02 = create_text("Action (A)", 10, 50, "black")
text_03 = create_text("Inventaire (I)", 10, 80, "black")
text_04 = create_text("Pièces (P) : ", 750, 20, "black")
text_05 = create_text("Etat des dinosaures (E)", 740, 570, "black")
t0 = [text_01, text_02, text_03, text_04, text_05]

text_11 = create_text("Pause", 110, 110, "red")
text_12 = create_text("Paramètres", 110, 140, "black")
text_13 = create_text("Quitter le jeu", 110, 170, "black")
text_14 = create_text("A propos de nous", 110, 200, "black")
text_15 = create_text("Télécharger notre rapport", 110, 230, "black")
t1 = [text_11, text_12, text_13, text_14, text_15]

text_21 = create_text("Nous vous transmettons nos plus sincères excuses, ", 110, 110, "red")
text_22 = create_text("De nombreuses zones de ce jeu sont encore en travaux, ", 110, 140, "black")
text_23 = create_text("Merci de bien vouloir recueillir nos plus grands regrets. Tony, Raphaël, Ibrahima, Farhane.", 110, 170, "black")
t2 = [text_21, text_22, text_23]

text_31 = create_text("Créateurs - Raphaël DALBAN-MOREYNAS, Ibrahima TOURE, Tony Gaël BIVAHAGUMYE, Farhane SABI YO", 110, 110, "red")
text_32 = create_text("Nous sommes un groupe d'étudiants en Sciences des Données, sur le campus universitaire Simone Veil, à Aurillac.", 110, 140, "black")
text_33 = create_text("Dans le cadre du Projet Tutoré, et en collaboration avec notre professeure de programmation, Morgane VIDAL, ", 110, 170, "black")
text_34 = create_text("nous avons réalisé ce jeu, où l'utilisateur doit gérer son propre parc de dinosaures.", 110, 200, "black")
text_35 = create_text("Pour toute question complémentaire, veuillez nous contacter via cette adresse : Raphael.DALBAN-MOREYNAS@etu.uca.fr.", 110, 230, "black")
t3 = [text_31, text_32, text_33, text_34, text_35]

text_41 = create_text("Notre rapport se trouve dans les fichiers internes du programme.", 110, 110, "red")
t4 = [text_41]

text_51 = create_text("Faire manger un dinosaure", 110, 110, "red")
text_52 = create_text("Faire un câlin à un dinosaure", 110, 140, "black")
text_53 = create_text("Soigner un dinosaure", 110, 170, "black")
t5 = [text_51, text_52, text_53]

text_61 = create_text("dino11", 110, 110, "red")
text_62 = create_text("dino12", 110, 140, "black")
text_63 = create_text("dino13", 110, 170, "black")
text_64 = create_text("dino14", 110, 200, "black")
t6 = [text_61, text_62, text_63, text_64]

text_71 = create_text("Acheter", 110, 110, "red")
text_72 = create_text("Vendre", 110, 140, "black")
t7 = [text_71, text_72]

text_81 = create_text("Dinosaures", 110, 110, "red")
text_82 = create_text("Potions", 110, 140, "black")
text_83 = create_text("Sorts", 110, 170 , "black")
t8 = [text_81, text_82, text_83]

text_91 = create_text("Normalosaure (10 P)", 110, 110, "red")
text_92 = create_text("Normalosaure évolué (50 P)", 110, 140, "black")
text_93 = create_text("Normalosaure titanesque (500 P)", 110, 170, "black")
text_94 = create_text("Redosaure (10 P)", 110, 200, "black")
text_95 = create_text("Redosaure évolué (60 P)", 110, 230, "black")
text_96 = create_text("Redosaure titanesque (90 P)", 110, 260, "black")
text_97 = create_text("Lavasaure (100 P)", 110, 290, "black")
text_98 = create_text("Lavasaure titanesque (500 P)", 110, 320, "black")
text_99 = create_text("Serpent-dinosaure Abyssal (1000 P)", 110, 350, "black")
text_910 = create_text("Roi-dinosaure (10000 P)", 110, 380, "black")
t9 = [text_91, text_92, text_93, text_94, text_95, text_96, text_97, text_98, text_99, text_910]

text_101 = create_text("Potion de rapidité (500 P)", 110, 110, "red")
text_102 = create_text("Potion de réduction de la faim (50 P)", 110, 140, "black")
text_103 = create_text("Potion de résistance à la dépression (500 P)", 110, 170, "black")
text_104 = create_text("Potion de résistance vitale (200 P)", 110, 200, "black")
text_105 = create_text("Potion de jolitude (10000 P)", 110, 230, "black")
t10 = [text_101, text_102, text_103, text_104, text_105]

text_111 = create_text("Cette zone est actuellement en travaux, veuillez contacter le SAV à cette adresse : Raphael.DALBAN-MOREYNAS@etu.uca.fr", 110, 110, "red")
t11 = [text_111]

text_121 = create_text("Suivre la faim des dinosaures", 110, 110, "red")
text_122 = create_text("Suivre la santé des dinosaures", 110, 140, "black")
text_123 = create_text("Suivre l'humeur des dinosaures", 110, 170, "black")
t12 = [text_121, text_122, text_123]

text_131 = create_text("", 0, 0, "red")
t13 = [text_131]

text_141 = create_text("", 0, 0, "red")
t14 = [text_141]

text_151 = create_text("", 0, 0, "red")
t15 = [text_151]