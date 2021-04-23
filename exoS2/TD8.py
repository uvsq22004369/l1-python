import tkinter as tk
racine = tk.Tk()
racine.title("Jeu de la vie")

CASES  = 10
COTE = 100
HEIGHT = 1000
WIDTH  = 1000

canvas = tk.Canvas(racine, height= HEIGHT, width= WIDTH, bg= "black")
canvas.grid(row=0, column=1)


etat_grille = [[0] * CASES for i in range(CASES)]

gestion_canvas = [[0] * CASES for i in range(CASES)]


def affiche_vivant(i,j):   #agit sur gestion_canvas et l'affichage du canevas 
    gestion_canvas[i][j] = canvas.create_rectangle((i*COTE,j*COTE),((i+1)*COTE,(j+1)*COTE), fill = "red")


def affiche_mort(i,j):   #agit sur gestion_canvas et l'affichage du canevas 
    canvas.delete(gestion_canvas[i][j])
    gestion_canvas[i][j] = 0


def modifie(event):
    i = event.x//COTE
    j = event.y//COTE
    global etat_grille
    if etat_grille[i][j]==0:
        etat_grille[i][j]=1
        affiche_vivant(i,j)
    else:
        etat_grille[i][j]=0
        affiche_mort


def regle_vie(i,j,etat_grille):
    count = - etat_grille[i][j]
    for i in range(i-1, i+2):
        for i in range(j-1, j+2):
            if etat_grille[i][j]==1:
                count+=1
    if count==1:
        etat_grille[i][j]=1
    elif count==2 and etat_grille[i][j]==1:
        etat_grille[i][j]=1
    else:
        etat_grille[i][j]=0
 

def update(ancien_etat,nouvel_etat):
    pass


jouer = tk.Button(racine, text= "Jouer", fg= "black")
jouer.grid(row=0, column=0)
stop = tk.Button(racine, text= "Stop", fg= "black")
stop.grid(row=0, column=0)
quitter = tk.Button(racine, text= "Quitter", fg= "black", command= racine.destroy)
quitter.grid(row=0, column=0)


racine.mainloop()