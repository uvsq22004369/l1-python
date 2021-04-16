#Cryptanalyse
#Votre mission, si vous l'acceptez, est de déchiffrer 4 textes de difficulté croissante en vous aidant d'un programme 
#python que vous allez écrire.

#Les fichiers ont été cryptés avec des méthodes données en cours.
#Les fichiers chiffrés contiennent des textes en ASCII. Une fois déchiffrés ils vous donneront des informations.
#Vous devez vous baser sur les fréquences d'apparition des lettres en français (et des paires de lettres) pour casser les codes. 
#Faire une fonction de calcul pour vous aider.

#Penser à réutliser le code du td de cryptographie comme base de travail.

#Le code de votre programme doit être sur github et vous fournirez un lien vers votre projet github avec le code et le résultat 
#du décodage en le déposant sur Moodle avant le mercredi 12 mai.
#Une soutenance sera organisée le 17 mai.

import tkinter as tk

texte1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
#le prochain fichier aura un code par substitution alphabetique  chaque lettre est remplacee par une autre: utiliser la frequence des lettres pour decoder le message.
texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
texte4 = "jeqeqecvnf suozvb jfk muj  dfjr fmy rvuqsk ve  itajtd mifwz nnrt  imtrvp zuh srzmzbqz tepr zn  tmsnirt imtrvp nec hw  dzpqj tjf pdecpr zl jr  ptejnt ekpb iu b  iiuyu iy ijz surg rjs ttsn  votp ac hw rzpuen jozw  rvwdvx jbo nirscyjv fi  svmkyw ve iaflss yie te  teffvv'u riznxjzvv jfk  nelrhtjrk dh sivdvjvve  yi cvb à jffrds tdp  rvwdv sebr onvnqsy zvp  zuhjwiM le wmifo wiezib nec  triot qmjvr'c onrwz  memfqg srq wdaietsq vk"
alphabet=[]

alphabet=[]

def alphabet_vide():
    for i in range(97, 122) :
       alphabet.append([chr(i),0.0])

def vide():
    for x in alphabet :
        x[1]=0.0

alphabet_vide()

def nbrOccur(texte) :
    vide()
    for c in texte : 
        if 97 <= ord(c) <= 122 : 
            alphabet[ord(c)-97][1] += round(1/len(texte),3)*100


nbrOccur(texte1)
print(alphabet)

def rang(lettre) :
    return ord(lettre)-97

def decalage(lettre1,lettre2):
    if  ord(lettre1) < 97 or ord(lettre1) > 122:
        return lettre1
    return chr(((rang(lettre1)+rang(lettre2))%26)+97)


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