import tkinter as tk

def decalage(lettre_message,lettre_cle):
    return chr(ord(lettre_message)+ord(lettre_cle) & ((1<<8)-1))

def dec_texte(texte,cle):
    texte_code = ""
    t, c = 0, 0
    while len(texte_code) < len(texte):
      texte_code += decalage(texte[t], cle[c])
      t, c = t + 1, c + 1
      if c == len(cle):
        c = 0
    return texte_code


def chiffre():
    resultat.delete(0, tk.END)
    if entree_texte.get() == "" or entree_cle.get() == "":
      resultat.insert(0, "Il manque quelque chose en entrée :/")
    resultat.insert(0, dec_texte(entree_texte.get(), entree_cle.get()))

# On peut aussi faire 2 fonction différente
#
#def chiffre():
#    resultat.delete(0,tk.END)
#    resultat.insert(0,dec_texte(entree_texte.get(),entree_cle.get()))
#
#def detect() :
#    if (entree_texte.get() == "" + entree_cle.get() == "") : 
#        resultat.insert(0),"Il manque des argument"

def dechiffrement(texte_a_decoder, cle):
    texte_decode = ""
    t, c = 0, 0
    while len(texte_decode) < len(texte_a_decoder):
      texte_decode += decalage(texte_a_decoder[t], chr(256-ord(cle[c])))
      t, c = t + 1, c + 1
      if c == len(cle):
        c = 0
    return texte_decode

def dechiffre():
    if entree_texte.get() == "" or entree_cle.get() == "":
      resultat.insert(0, "Il manque quelque chose en entrée :/")
    else:
      label_res.config(text = dechiffrement(resultat.get(), entree_cle.get()))

def chiffre_xor(lettre_message,lettre_cle):
    return (chr(ord(lettre_message) ^ ord(lettre_cle)))







racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

bouton_coder=tk.Button(racine, text="Chiffrer texte",fg="black", width=15, command=chiffre)
bouton_coder.grid(row=2, column=0)

bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=dechiffre)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)

label_res=tk.Label(racine,font = ("helvetica", "20"), text="Déchiffement ici.")
label_res.grid(row = 3, column=1)

racine.mainloop()