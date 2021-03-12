## BI TD02        ##
## Océane Machado ##
## 22004369       ##

#Importation
import tkinter as tk
root = tk.Tk()
root.title("Petit Photoshop")
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import filedialog
from tkinter import simpledialog



#Constante
create=True
nomImgCourante=""



#Fonction
def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return(len(matrice))

def saving(matPix, filename):
    toSave = pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)

def loading(filename):
    toLoad = pil.Image.open(filename)
    mat = [[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat

def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    filename = filedialog.askopenfile(mode = 'rb', title = 'Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante = filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image = photo)
        canvas.grid(row = 0,column = 1,rowspan = 4,columnspan = 2)
        create=False
        
    else:
        canvas.grid_forget()
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin=canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)

def modify(matrice):
    global imgModif
    global nomImgCourante
    saving(matrice,"modif.png")
    imgModif=ImageTk.PhotoImage(file="modif.png")
    canvas.itemconfigure(dessin, image=imgModif)
    nomImgCourante="modif.png"

def filtre_vert():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(0,mat[i][j][1],0,255)
    modify(mat)
            
def negatif():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=(255-mat[i][j][0],255-mat[i][j][1],255-mat[i][j][2],255)
    modify(mat)
            
def symetrique():
    mat = loading(nomImgCourante)
    matSym = [[(0,0,0,0)]*nbrCol(mat) for k in range(nbrLig(mat))]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            matSym[i][nbrCol(mat)-1-j]=mat[i][j]
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            mat[i][j]=matSym[i][j]
    modify(mat)

def gris():
    mat = loading(nomImgCourante)
    for i in range(nbrLig(mat)):
        for j in range(nbrCol(mat)):
            gris = int(mat[i][j][0]*0.2125 + mat[i][j][1]*0,7154 + mat[i][j][2]*0,0721)
    mat[i][j] = (gris, gris, gris, 255)
    modify(mat)

def quitter():
    root.destroy()

def rotation() :
    mat = loading(nomImgCourante)
    matSym = [[(0,0,0,0)]*nbrLig(mat) for k in range(nbrCol(mat))]
    for j in range(nbrCol(mat)):
        for i in range(nbrLig(mat)):
            matSym[j][nbrLig(mat)-1-i]=mat[j][i]
    for j in range(nbrLig(mat)):
        for i in range(nbrCol(mat)):
            mat[i][j]=matSym[j][i]
    modify(mat)




#Programme Principal
vert = tk.Button(root, text = "Filtre Vert", command = filtre_vert )
vert.grid(column = 0, row = 0)

negatif = tk.Button(root, text = "Filtre Négatif", command = negatif )
negatif.grid(column = 0, row = 1)

symetrique = tk.Button(root, text = "Symétrique", command = symetrique )
symetrique.grid(column = 0, row = 2)

gris = tk.Button(root, text = "Filtre Noir et Blanc", command = gris )
gris.grid(column = 0, row = 3)

rotat90 = tk.Button(root, text = "Rotation 90°", command = rotation )
rotat90.grid(column = 0, row = 4)

charg = tk.Button(root, text = "Charger Image", command = lambda:charger(root))
charg.grid(column = 0, row = 5)

quitter = tk.Button(root, text = "Quitter", command = quitter )
quitter.grid(column = 1, row = 5)

root.mainloop()