##################################################
# Projet Robot Ricochet
# Groupe BI: 1
# Mathieu LAM
# Océane MACHADO
# Aurélie ALVET
# Timothé PEYREIGNE
# Thushanth JEYAKANTHN
# Yanis MERBAH
# https://github.com/uvsq21915611/projet_robot
###################################################

import tkinter as tk
from tkinter.constants import END, LEFT
racine = tk.Tk()
racine.title("Projet robot ricochet")
racine.configure(width = 300, height = 300, bg ='beige')

c = 50                         # Longueur d'un côté d'une case
n = 16                         # Nombre de cases par ligne et par colonne
cases = []
WIDTH = n*c+2
HEIGHT = WIDTH
couleur = ""

# position initiale des robots
X1 = 177
Y1 = 577
X2 = 427
Y2 = 477
X3 = 477
Y3 = 327
X4 = 75
Y4 = 625


#Crée les robot et leurs paramètres
def robot_rouge():
    couleur = "rouge"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X2-rayon, Y2-rayon),
                                (X2+rayon, Y2+rayon),
                                fill="red")
    return [cercle, dx, dy]

def robot_jaune():
    couleur = "jaune"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X4-rayon, Y4-rayon),
                                (X4+rayon, Y4+rayon),
                                fill="yellow")
    return [cercle, dx, dy]

def robot_vert():
    couleur = "vert"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X1-rayon, Y1-rayon),
                                (X1+rayon, Y1+rayon),
                                fill="green")
    return [cercle, dx, dy]

def robot_bleu():
    couleur = "bleu"
    dx, dy = 1, 2
    rayon = 20
    cercle = canvas.create_oval((X3-rayon, Y3-rayon),
                                (X3+rayon, Y3+rayon),
                                fill="blue")

    return [cercle, dx, dy]

#Définit quel robot de couleur est actuellement sélectionné
def selectionne(event):
    pass


#Associe les touches directionnelles du clavier "haut","bas","gauche","droite" au déplacement du robot
def Clavier(event):
    global X1, X2, X3, X4, Y1, Y2, Y3, Y4
    touche = event.keysym
    print(touche)
    # déplacement vers le haut
    if touche == 'Up':
        Y1 -= 200
        Y2 -= 200 
        Y3 -= 200
        Y4 -= 200
    # déplacement vers le bas
    if touche == 'Down':
        if selectionne == robot_rouge :
            Y2 += 200
        elif selectionne == robot_bleu :
            Y3 += 200
        elif selectionne == robot_jaune :
            Y4 += 200
        elif selectionne == robot_vert :
            Y1 += 200
    # déplacement vers la droite
    if touche == 'Right':
        if selectionne == robot_rouge :
            X2 += 200
        elif selectionne == robot_bleu :
            X3 += 200
        elif selectionne == robot_jaune :
            X4 += 200
        elif selectionne == robot_vert :
            X1 += 200
    # déplacement vers la gauche
    if touche == 'Left':
        if selectionne == robot_rouge :
            X2 -= 200
        elif selectionne == robot_bleu :
            X3 -= 200
        elif selectionne == robot_jaune :
            X4 -= 200
        elif selectionne == robot_vert :
            X1 -= 200
    # on dessine le pion à sa nouvelle position
    canvas.coords(robot_vert, X1-10, Y1-10, X1+10, Y1+10)
    canvas.coords(robot_rouge, X2-100, Y2-100, X2+100, Y2+100)
    canvas.coords(robot_bleu, X3-10, Y3-10, X3+10, Y3+10)
    canvas.coords(robot_jaune, X4-10, Y4-10, X4+10, Y4+10)


#Permet de faire arrêter le robot s'il rencontre un obstacle / distance maximale de déplacement autorisé
def bounce():
    pass

#Affiche un rectangle de couleur permettant de montrer les directions possibles par le robot 
def show_Path():
    pass

#Fait recommencer le jeu
def reset():
    pass
    

#Affiche le score / liste des meilleurs scores
def score():
    pass

#Affiche le nombre de mouvements effectués
def compteur():
    pass

#Permet d'enregistrer l'état de la partie (position des robots/nombres de mouvements/ ect ... )
def save():
    pass

#Permet de charger les éléments précédemment sauvegardés
def load():
    pass

#Permet d'éditer le plateau en rajoutant des éléments 
def editor():
    pass


#Permet d'afficher les dernier mouvement fait
def move(event):
    touche = event.keysym
    if touche == 'Up':
        print("Up") 
    if touche == 'Down':
        print("Down") 
    if touche == 'Right':
        print("Right") 
    if touche == 'Left':
        print("Left")





canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
canvas.grid(row=1, column=0)
canvas.bind('<Key>', Clavier)


canvas_move = tk.Canvas(racine, width= WIDTH/5, height= HEIGHT, bg="black")
canvas_move.bind('Key', move)
canvas_move.grid(row=1, column=1)


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

robot_rouge()

sauvegarde = tk.Button(racine, text="sauvegarder", command=save())
sauvegarde.grid(row=1, column= 3)




racine.mainloop()
