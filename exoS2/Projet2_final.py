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
racine = tk.Tk()
racine.title("Projet Robot Ricochet")
racine.configure(width = 500, height = 500, bg ='beige')

#variable
c = 40                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH
stop = False
# position initiale des robots
PosX1 = 142
PosY1 = 463
PosX2 = 342
PosY2 = 382
PosX3 = 382
PosY3 = 262
PosX4 = 61
PosY4 = 502


#Fonction

def est_dans_carre(x, y):
    """Retourne True si le point de coordonnées (x, y)
    est dans le rectangle et False sinon"""
    return 350 + 2 < x < 450 + 2 and 350 + 2 < y < 450 + 2


def reset(event):
    """Recommence la partie si clic sur le carre"""
    global stop
    if est_dans_carre(event.x, event.y) and not stop:
        pass
    else:
        stop = True

def save():
    """ Sauvegarde la partie en cours """
    pass

def color(fill):
    fill = ''


#Définit quel robot de couleur est actuellement sélectionné
def selectionne(event):
    """ Permet de faire la selection d'un pion pour le bouger """
    pass

#Permet de faire arrêter le robot s'il rencontre un obstacle / distance maximale de déplacement autorisé
def collision(robot, obstacle):
    """ Fait s'arreter le robots lorsqu'il rencontre un obstacle """
    if robot['x'] >= obstacle['x'] + obstacle['longueur'] or \
       robot['x'] + robot['longueur'] <= obstacle['x'] or \
       robot['y'] >= obstacle['y'] + obstacle['hauteur'] or \
       robot['y'] + robot['hauteur'] <= obstacle['y']:
        return False
    return True

def Clavier(event):
    """ Gestion de l'événement Appui sur une touche du clavier """
    global PosX1, PosY1, PosX2, PosY2, PosX3, PosY3, PosX4, PosY4
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'Up':
        PosY1 -= 40
        PosY2 -= 40 
        PosY3 -= 40
        PosY4 -= 40
    # déplacement vers le bas
    if touche == 'Down':
        PosY1 += 40
        PosY2 += 40
        PosY3 += 40
        PosY4 += 40
    # déplacement vers la droite
    if touche == 'Right':
        PosX1 += 40
        PosX2 += 40
        PosX3 += 40
        PosX4 += 40
    # déplacement vers la gauche
    if touche == 'Left':
        PosX1 -= 40
        PosX2 -= 40
        PosX3 -= 40
        PosX4 -= 40
    # on dessine le pion à sa nouvelle position
    canvas.coords(PionV,PosX1 -15, PosY1 -15, PosX1 +15, PosY1 +15)
    canvas.coords(PionR,PosX2 -15, PosY2 -15, PosX2 +15, PosY2 +15)
    canvas.coords(PionB,PosX3 -15, PosY3 -15, PosX3 +15, PosY3 +15)
    canvas.coords(PionJ,PosX4 -15, PosY4 -15, PosX4 +15, PosY4 +15)





# Création d'un widget Canvas (zone graphique)
canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
PionV = canvas.create_oval(PosX1-15, PosY1-15, PosX1+15, PosY1+15, width=2, fill='green')
PionR = canvas.create_oval(PosX2-15, PosY2-15, PosX2+15, PosY2+15, width=2, fill='red')
PionB = canvas.create_oval(PosX3-15, PosY3-15, PosX3+15, PosY3+15, width=2, fill='blue')
PionJ = canvas.create_oval(PosX4-15, PosY4-15, PosX4+15, PosY4+15, width=2, fill='yellow')
canvas.focus_set()
canvas.bind('<Key>',Clavier)
canvas.grid(row =1, column =0)

#création grille
for ligne in range(n):
    transit = []
    for colonne in range(n):
        transit.append(canvas.create_rectangle(colonne*c+2, ligne*c+2, (colonne+1)*c+2, (ligne+1)*c+2))
    cases.append(transit)

mur_vertical1 = canvas.create_rectangle(200-2, 0, 200+5, 40+2, fill="black")
mur_vertical2 = canvas.create_rectangle(480-2, 0, 480+5, 40+2, fill="black")
mur_vertical3 = canvas.create_rectangle(280-2, 40+2, 280+5, 80+2, fill="black")
mur_vertical4 = canvas.create_rectangle(40-2, 80+2, 40+5, 120+2, fill="black")
mur_vertical5 = canvas.create_rectangle(480-2, 80+2, 480+5, 120+2, fill="black")
mur_vertical6 = canvas.create_rectangle(560-2, 120+2, 560+5, 160+2, fill="black")
mur_vertical7 = canvas.create_rectangle(400-2, 160+2, 400+5, 200+2, fill="black")
mur_vertical8 = canvas.create_rectangle(280-2, 200+2, 280+5, 240+2, fill="black")
mur_vertical9 = canvas.create_rectangle(480-2, 200+2, 480+5, 240+2, fill="black")
mur_vertical10 = canvas.create_rectangle(80-2, 240+2, 80+5, 240+2, fill="black")
mur_vertical11 = canvas.create_rectangle(520-2, 360+2, 520+5, 400+2, fill="black")
mur_vertical12 = canvas.create_rectangle(160-2, 400+2, 160+5, 440+2, fill="black")
mur_vertical13 = canvas.create_rectangle(240-2, 440+2, 240+5, 480+2, fill="black")
mur_vertical14 = canvas.create_rectangle(80-2, 480+2, 80+5, 520+2, fill="black")
mur_vertical15 = canvas.create_rectangle(360-2, 480+2, 360+5, 520+2, fill="black")
mur_vertical16 = canvas.create_rectangle(160-2, 520+2, 160+5, 560+2, fill="black")
mur_vertical17 = canvas.create_rectangle(560-2, 520+2, 560+5, 560+2, fill="black")
mur_vertical18 = canvas.create_rectangle(480-2, 560+2, 480+5, 600+2, fill="black")
mur_vertical19 = canvas.create_rectangle(160-2, 600+2, 160+5, 640, fill="black")
mur_vertical20 = canvas.create_rectangle(560-2, 600+2, 560+5, 640, fill="black")

mur_horizontal1 = canvas.create_rectangle(40+2, 80-2, 80+2, 80+5, fill="black")
mur_horizontal2 = canvas.create_rectangle(240+2, 80-2, 280+2, 80+5, fill="black")
mur_horizontal3 = canvas.create_rectangle(440+2, 120-2, 480+2, 120+5, fill="black")
mur_horizontal4 = canvas.create_rectangle(520+2, 120-2, 560+2, 120+5, fill="black")
mur_horizontal5 = canvas.create_rectangle(240+2, 200-2, 280+2, 200+5, fill="black")
mur_horizontal6 = canvas.create_rectangle(400+2, 200-2, 440+2, 200+5, fill="black")
mur_horizontal7 = canvas.create_rectangle(480+2, 200-2, 520+2, 200+5, fill="black")
mur_horizontal8 = canvas.create_rectangle(0,240-2, 40+2, 240+5, fill="black")
mur_horizontal9 = canvas.create_rectangle(600+2, 240-2, 640+2, 240+5, fill="black")
mur_horizontal10 = canvas.create_rectangle(80+2, 280-2, 120+2, 280+5, fill="black")
mur_horizontal11 = canvas.create_rectangle(480+2, 360-2, 520+2, 360+5, fill="black")
mur_horizontal12 = canvas.create_rectangle(0, 400-2, 40+2, 400+5, fill="black")
mur_horizontal13 = canvas.create_rectangle(600+2, 400-2, 640+2, 400+5, fill="black")
mur_horizontal14 = canvas.create_rectangle(120+2, 440-2, 160+2, 440+5, fill="black")
mur_horizontal15 = canvas.create_rectangle(200+2, 440-2, 240+2, 440+5, fill="black")
mur_horizontal16 = canvas.create_rectangle(360+2, 480-2, 400+2, 480+5, fill="black")
mur_horizontal17 = canvas.create_rectangle(80+2, 520-2, 120+2, 520+5, fill="black")
mur_horizontal18 = canvas.create_rectangle(160+2, 520-2, 200+2, 520+5, fill="black")
mur_horizontal19 = canvas.create_rectangle(560+2, 560-2, 600+2, 560+5, fill="black")
mur_horizontal20 = canvas.create_rectangle(440+2, 600-2, 480+2, 600+5, fill="black")

carre_restart = canvas.create_rectangle(280+2, 280+2, 360+2, 360+2, fill="black")




#Bouton label etc...
# Création d'un widget Button (bouton Quitter)
quitter = tk.Button(racine, text ='Quitter', command = racine.destroy)
quitter.grid(row=6, column=0)
# Création d'un label Button (manière de jouer)
explication = tk.Label(racine, text ='Selectionne un pion avec ta souris puis utilise les fléches de ton clavier pour déplacer.')
explication.grid(row=0, column=0)

sauvegarde = tk.Button(racine, text="sauvegarder", command=save())
sauvegarde.grid(row=0, column= 0)

texte_compteur = tk.Label(racine, text="Nombre de déplacements:  ")
texte_compteur.grid(row=0, column=3)

texte_resultat = tk.Label(racine, text="Jeu résolu: NON", bg="red", fg="white")
texte_resultat.grid(row=0, column=2)


racine.mainloop()








