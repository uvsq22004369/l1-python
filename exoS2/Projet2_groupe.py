###################################################
# Groupe BI: 1                                    #
# Mathieu LAM                                     #
# Océane MACHADO                                  #
# Aurélie ALVET                                   #
# Timothé PEYREIGNE                               #
# Thushanth JEYAKANTHN                            #
# Merbah Yanis                                    #
# 
###################################################


#import des librairies


import tkinter as tk
from tkinter.constants import END, LEFT
fenetre = tk.Tk()
fenetre.title("Projet Robot Ricochet")
fenetre.configure(width = 300, height = 300, bg ='beige')
       

c = 50                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    #rebond()
    pass


def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX1, PosY1, PosX2, PosY2, PosX3, PosY3, PosX4, PosY4
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'Up':
        PosY1 -= 20
        PosY2 -= 20 
        PosY3 -= 20
        PosY4 -= 20
    # déplacement vers le bas
    if touche == 'Down':
        PosY1 += 20
        PosY2 += 20
        PosY3 += 20
        PosY4 += 20
    # déplacement vers la droite
    if touche == 'Right':
        PosX1 += 20
        PosX2 += 20
        PosX3 += 20
        PosX4 += 20
    # déplacement vers la gauche
    if touche == 'Left':
        PosX1 -= 20
        PosX2 -= 20
        PosX3 -= 20
        PosX4 -= 20
    # on dessine le pion à sa nouvelle position
    canvas.coords(PionV,PosX1 -10, PosY1 -10, PosX1 +10, PosY1 +10, command = mouvement())
    canvas.coords(PionR,PosX2 -10, PosY2 -10, PosX2 +10, PosY2 +10, command = mouvement())
    canvas.coords(PionB,PosX3 -10, PosY3 -10, PosX3 +10, PosY3 +10, command = mouvement())
    canvas.coords(PionJ,PosX4 -10, PosY4 -10, PosX4 +10, PosY4 +10, command = mouvement())





# position initiale du pion
PosX1 = 177
PosY1 = 577
PosX2 = 427
PosY2 = 477
PosX3 = 477
PosY3 = 327
PosX4 = 75
PosY4 = 625

# Création d'un widget Canvas (zone graphique)
Largeur = 100
Hauteur = 100
canvas = tk.Canvas(fenetre, width=WIDTH, height=HEIGHT, bg="white")
PionV = canvas.create_oval(PosX1-20,PosY1-20,PosX1+20,PosY1+20,width=2,outline='black',fill='green')#, select= False)
PionR = canvas.create_oval(PosX2-20,PosY2-20,PosX2+20,PosY2+20,width=2,outline='black',fill='red')#, select= False)
PionB = canvas.create_oval(PosX3-20,PosY3-20,PosX3+20,PosY3+20,width=2,outline='black',fill='blue')#, select= False)
PionJ = canvas.create_oval(PosX4-20,PosY4-20,PosX4+20,PosY4+20,width=2,outline='black',fill='yellow')#, select= False)
canvas.focus_set()
canvas.bind('<Key>',Clavier)
canvas.grid(row =1, column =0)

for ligne in range(n):
    transit = []
    for colonne in range(n):
        transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)

mur_vertical1 = canvas.create_rectangle(250-2, 0, 250+5, 50+2, fill="black")
mur_vertical2 = canvas.create_rectangle(600-2, 0, 600+5, 50+2, fill="black")
mur_vertical3 = canvas.create_rectangle(350-2, 50+2, 350+5, 100+2, fill="black")
mur_vertical4 = canvas.create_rectangle(50-2, 100+2, 50+5, 150+2, fill="black")
mur_vertical5 = canvas.create_rectangle(600-2, 100+2, 600+5, 150+2, fill="black")
mur_vertical6 = canvas.create_rectangle(700-2, 150+2, 700+5, 200+2, fill="black")
mur_vertical7 = canvas.create_rectangle(500-2, 200+2, 500+5, 250+2, fill="black")
mur_vertical8 = canvas.create_rectangle(350-2, 250+2, 350+5, 300+2, fill="black")
mur_vertical9 = canvas.create_rectangle(600-2, 250+2, 600+5, 300+2, fill="black")
mur_vertical10 = canvas.create_rectangle(100-2, 300+2, 100+5, 350+2, fill="black")
mur_vertical11 = canvas.create_rectangle(650-2, 450+2, 650+5, 500+2, fill="black")
mur_vertical12 = canvas.create_rectangle(200-2, 500+2, 200+5, 550+2, fill="black")
mur_vertical13 = canvas.create_rectangle(300-2, 550+2, 300+5, 600+2, fill="black")
mur_vertical14 = canvas.create_rectangle(100-2, 600+2, 100+5, 650+2, fill="black")
mur_vertical15 = canvas.create_rectangle(450-2, 600+2, 450+5, 650+2, fill="black")
mur_vertical16 = canvas.create_rectangle(200-2, 650+2, 200+5, 700+2, fill="black")
mur_vertical17 = canvas.create_rectangle(700-2, 650+2, 700+5, 700+2, fill="black")
mur_vertical18 = canvas.create_rectangle(600-2, 700+2, 600+5, 750+2, fill="black")
mur_vertical19 = canvas.create_rectangle(200-2, 750+2, 200+5, 800, fill="black")
mur_vertical20 = canvas.create_rectangle(700-2, 750+2, 700+5, 800, fill="black")

mur_horizontal1 = canvas.create_rectangle(50+2, 100-2, 100+2, 100+5, fill="black")
mur_horizontal2 = canvas.create_rectangle(300+2, 100-2, 350+2, 100+5, fill="black")
mur_horizontal3 = canvas.create_rectangle(550+2, 150-2, 600+2, 150+5, fill="black")
mur_horizontal4 = canvas.create_rectangle(650+2, 150-2, 700+2, 150+5, fill="black")
mur_horizontal5 = canvas.create_rectangle(300+2, 250-2, 350+2, 250+5, fill="black")
mur_horizontal6 = canvas.create_rectangle(500+2, 250-2, 550+2, 250+5, fill="black")
mur_horizontal7 = canvas.create_rectangle(600+2, 250-2, 650+2, 250+5, fill="black")
mur_horizontal8 = canvas.create_rectangle(0, 300-2, 50+2, 300+5, fill="black")
mur_horizontal9 = canvas.create_rectangle(750+2, 300-2, 800+2, 300+5, fill="black")
mur_horizontal10 = canvas.create_rectangle(100+2, 350-2, 150+2, 350+5, fill="black")
mur_horizontal11 = canvas.create_rectangle(600+2, 450-2, 650+2, 450+5, fill="black")
mur_horizontal12 = canvas.create_rectangle(0, 500-2, 50+2, 500+5, fill="black")
mur_horizontal13 = canvas.create_rectangle(750+2, 500-2, 800+2, 500+5, fill="black")
mur_horizontal14 = canvas.create_rectangle(150+2, 550-2, 200+2, 550+5, fill="black")
mur_horizontal15 = canvas.create_rectangle(250+2, 550-2, 300+2, 550+5, fill="black")
mur_horizontal16 = canvas.create_rectangle(450+2, 600-2, 500+2, 600+5, fill="black")
mur_horizontal17 = canvas.create_rectangle(100+2, 650-2, 150+2, 650+5, fill="black")
mur_horizontal18 = canvas.create_rectangle(200+2, 650-2, 250+2, 650+5, fill="black")
mur_horizontal19 = canvas.create_rectangle(700+2, 700-2, 750+2, 700+5, fill="black")
mur_horizontal20 = canvas.create_rectangle(550+2, 750-2, 600+2, 750+5, fill="black")

carre_restart = canvas.create_rectangle(350+2, 350+2, 450+2, 450+2, fill="black")



# Création d'un widget Button (bouton Quitter)
quitter = tk.Button(fenetre, text ='Quitter', command = fenetre.destroy)
quitter.grid(row=6, column=0)
# Création d'un label Button (manière de jouer)
explication = tk.Label(fenetre, text ='Selectionne un pion avec ta souris puis utilise les fléches de ton clavier pour déplacer.')
explication.grid(row=0, column=0)


fenetre.mainloop()







        if selectionne == robot_rouge :
            y -= 20
        elif selectionne == robot_bleu :
            y -= 20 
        elif selectionne == robot_jaune :
            y -= 20
        elif selectionne == robot_vert :
            y -= 20
