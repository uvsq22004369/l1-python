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
fenetre.configure(width = 500, height = 500, bg ='beige')



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
    Canevas.coords(PionV,PosX1 -10, PosY1 -10, PosX1 +10, PosY1 +10)
    Canevas.coords(PionR,PosX2 -10, PosY2 -10, PosX2 +10, PosY2 +10)
    Canevas.coords(PionB,PosX3 -10, PosY3 -10, PosX3 +10, PosY3 +10)
    Canevas.coords(PionJ,PosX4 -10, PosY4 -10, PosX4 +10, PosY4 +10)



# position initiale du pion
PosX1 = 10
PosY1 = 10
PosX2 = 80
PosY2 = 60
PosX3 = 30
PosY3 = 70
PosX4 = 90
PosY4 = 100

# Création d'un widget Canvas (zone graphique)
Largeur = 100
Hauteur = 100
Canevas = tk.Canvas(fenetre, width = Largeur, height =Hauteur, bg ='white')
PionV = Canevas.create_oval(PosX1-9,PosY1-9,PosX1+9,PosY1+9,width=2,outline='black',fill='green')#, select= False)
PionR = Canevas.create_oval(PosX2-9,PosY2-9,PosX2+9,PosY2+9,width=2,outline='black',fill='red')#, select= False)
PionB = Canevas.create_oval(PosX3-9,PosY3-9,PosX3+9,PosY3+9,width=2,outline='black',fill='blue')#, select= False)
PionJ = Canevas.create_oval(PosX4-9,PosY4-9,PosX4+9,PosY4+9,width=2,outline='black',fill='yellow')#, select= False)
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.grid(row =1, column =0)

# Création d'un widget Button (bouton Quitter)
quitter = tk.Button(fenetre, text ='Quitter', command = fenetre.destroy)
quitter.grid(row=6, column=0)
# Création d'un label Button (manière de jouer)
explication = tk.Label(fenetre, text ='Selectionne un pion avec ta souris puis utilise les fléches de ton clavier pour déplacer.')
explication.grid(row=0, column=0)


fenetre.mainloop()








