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
root = tk.Tk()
root.title("Projet Robot Ricochet")

def fin ():
    root.quit()
    root.destroy()
 
def grille():
    for i in range(nbcase+1):
        Can.create_line(x0+case*i, y0,x0+case*i,y0 + nbcase*case)
        Can.create_line(x0, y0+case*i,x0+nbcase*case ,y0+case*i)
 

 
def jouer(event):
    global trouve
    [i,j]=correspond(event.x,event.y)
    if i in range(nb) and j in range (nb):   # on ne fait rien si le click est hors grille
        Can.create_rectangle(x0 +c*j,y0+c*i,x0 +c*(j+1),y0+c*(i+1),fill=coul(i,j))
 
 

 
Texte1.grid(root , row=0,column=0)
BouttonQuit.grid(root, row=50, column=100)
Cadre.grid(root, row=1,column=0)
BouttonJouer.grid(root, row=0, column=50)
TexteC.grid(root, row=1, column=3)
 

 



root.mainloop 








