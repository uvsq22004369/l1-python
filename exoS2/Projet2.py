###################################################
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# Merbah Yanis
# https://github.com/uvsq22004307/projet_incendie
###################################################



#import des librairies

import tkinter as tk
from tkinter.constants import END, LEFT
fenetre = tk.Tk()
fenetre.title("Projet Robot Ricochet")
fenetre.configure(width = 500, height = 500, bg ='grey')


def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX,PosY
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'z':
        PosY -= 477
    # déplacement vers le bas
    if touche == 's':
        PosY += 477
    # déplacement vers la droite
    if touche == 'd':
        PosX += 477
    # déplacement vers la gauche
    if touche == 'q':
        PosX -= 477
    # on dessine le pion à sa nouvelle position
    Canevas.coords(Pion,PosX -10, PosY -10, PosX +10, PosY +10)


# position initiale du pion
PosX = 120
PosY = 150

# Création d'un widget Canvas (zone graphique)
Largeur = 500
Hauteur = 500
Canevas = tk.Canvas(fenetre, width = Largeur, height =Hauteur, bg ='white')
Pion = Canevas.create_oval(PosX-10,PosY-10,PosX+10,PosY+10,width=2, fill='red')
Canevas.create_line(550,0,0,0, width=10, fill='black')#bon
Canevas.create_line(0,0,0,0, width=10, fill='black')
Canevas.create_line(0,0,0,0, width=10, fill='black')
Canevas.create_line(0,0,0,550, width=10, fill='black')#bon
Canevas.focus_set()
Canevas.bind('<Key>',Clavier)
Canevas.grid(row=2, column =0)

# Création d'un widget Button (bouton Quitter)
quitter = tk.Button(fenetre, text ='Quitter', command = fenetre.destroy)
quitter.grid(row=6, column=0)

explication = tk.Label(fenetre, text ='apuie sur z pour monté, s pour descendre, q pour aller à gauche et d pour aller a droite.')
explication.grid(row=0, column=0)


fenetre.mainloop()








