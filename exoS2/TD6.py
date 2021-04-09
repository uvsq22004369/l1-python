import tkinter as tk
import PIL as pil
from PIL import Image
from PIL import ImageTk 
from tkinter import Canvas, filedialog
from tkinter import simpledialog

def nbrCol(matrice):
    return(len(matrice[0]))

def nbrLig(matrice):
    return len(matrice)

def saving(matPix, filename):
    toSave=pil.Image.new("RGBA",(nbrCol(matPix),nbrLig(matPix)))
    for i in range(nbrCol(matPix)):
        for j in range(nbrLig(matPix)):
            toSave.putpixel((i,j),matPix[j][i])
    toSave.save(filename)


def loading(filename):
    toLoad=pil.Image.open(filename)
    mat=[[(255,255,255,255)]*toLoad.size[0] for k in range(toLoad.size[1])]
    for i in range(toLoad.size[1]):
        for j in range(toLoad.size[0]):
            mat[i][j]=toLoad.getpixel((j,i))
    return mat

create=True
nomImgCourante=""

def charger(widg):
    global create
    global photo
    global img
    global canvas
    global dessin
    global nomImgCourante
    filename= filedialog.askopenfile(mode='rb', title='Choose a file')
    img = pil.Image.open(filename)
    nomImgCourante=filename.name
    photo = ImageTk.PhotoImage(img)
    if create:    
        canvas = tk.Canvas(widg, width = img.size[0], height = img.size[1])
        dessin = canvas.create_image(0,0,anchor = tk.NW, image=photo)
        canvas.grid(row=0,column=1,rowspan=4,columnspan=2)
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


def fermer_fenetre():
    affi.destroy()

def derniers_bits(x,k): #renvoie les k derniers bits de x
    pass

print(derniers_bits(15,3))

def encoder_kbits(x,y,k): #remplace les k derniers bits de x par ceux de y
    pass

print(encoder_kbits(15,8,3))

def encoder_entier(e,pixel):  #encode un entier e sur 8 bits dans les bits de poids faible d'un pixel
    pass

def coder():
    texte_a_cacher = entree.get()
    mat=loading(nomImgCourante)
    #Choisir un ordre sur les pixels pour encoder le message
    modify(mat)


def decoder_pixel(pixel):
    res = (derniers_bits(pixel[2],2) << 6) + (derniers_bits(pixel[1],3) << 3) + (derniers_bits(pixel[0],3))
    return res


def decoder():
    mat=loading(nomImgCourante)
    sortie = ""
    

    label_decodage.config(text= sortie)



affi=tk.Tk()
affi.title("Stéganographie")

entree = tk.Entry(affi, width = 20  ,font = ("helvetica", "20"))
entree.grid(row = 0, column = 0)


bouton_coder=tk.Button(affi, text="Coder texte",fg="black", width=15, command=coder)
bouton_coder.grid(row=1,column=0)

bouton_decoder=tk.Button(affi,text="Décoder texte",fg="black",  width=15,command=decoder)
bouton_decoder.grid(row=2,column=0)

label_decodage=tk.Label(affi, text = "Décode moi !")
label_decodage.grid(row=3,column=0)

bouton = tk.Button(affi, text="Charger", fg="black", width=15, command=lambda :charger(affi))
bouton.grid(row=5,column=0)

btn = tk.Button(affi, text="Quitter", fg="black", width=8, command=fermer_fenetre)
btn.grid(row=5,column=2, sticky='E')

affi.mainloop()