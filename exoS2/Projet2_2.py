import tkinter as tk
import numpy as np
import PIL as pil

colors = ["rouge",  "jaune", "vert", "bleu"]

def fermer_fenetre():
    racine.destroy()


def robot_couleur_rouge():
    
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 2, 4
    rayon = 10
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="rouge")
    return [cercle, dx, dy]

def robot_couleur_jaune():
    
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 2, 4
    rayon = 10
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="jaune")
    return [cercle, dx, dy]

def robot_couleur_vert():
    
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 2, 4
    rayon = 10
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="vert")
     return [cercle, dx, dy]

def robot_couleur_bleu():
    
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 2, 4
    rayon = 10
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="bleu")

    return [cercle, dx, dy]


def carre():
    global objets
    x = rd.randint(0, 100)
    y = rd.randint(0, 100)
    objets.append(canvas.create_rectangle((x, y), (x+100, y+100), fill=""))



def mouvement():





def undo():
     repeat =
    if 
        for i in range(repeat):
            canvas.delete()
            del()

cpt=0          
def compteur(event):
    global cpt
    ? =str(cpt)
    cpt = cpt + 1





root = tk.Tk()
root.title("Projet Robot Ricochet")

root.geometry("600x600")
container = tk.Frame(root, bg = "white")
container.pack(expand = True, fill = "both")
drawArea = tk.Canvas(container, bg = "gray")
drawArea.pack()


bouton = tk.Button(racine, text="Quitter", fg="red",command=fermer_fenetre)
bouton.grid(column=0, row=1)

bouton_undo = tk.Button(racine, text="Undo", fg="red", command=undo)
bouton_undo.grid(row=0, column=2)

label = tk.Label(racine, text=str(cpt))
label.grid(column=0, row=3)

canvas.bind("<Button-1>", compteur)

root.mainloop()