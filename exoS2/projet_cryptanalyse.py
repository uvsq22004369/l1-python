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



texte1 = "kd oqnbgzhm ehbghdq ztqz tm bncd ozq rtarshstshnm zkogzadshptd: bgzptd kdssqd drs qdlokzbdd ozq tmd ztsqd. tshkhrdq kz eqdptdmbd cdr kdssqdr ontq cdbncdq kd ldrrzfd."
texte2 = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."
texte3 = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
texte4 = "jeqeqecvnf suozvb jfk muj  dfjr fmy rvuqsk ve  itajtd mifwz nnrt  imtrvp zuh srzmzbqz tepr zn  tmsnirt imtrvp nec hw  dzpqj tjf pdecpr zl jr  ptejnt ekpb iu b  iiuyu iy ijz surg rjs ttsn  votp ac hw rzpuen jozw  rvwdvx jbo nirscyjv fi  svmkyw ve iaflss yie te  teffvv'u riznxjzvv jfk  nelrhtjrk dh sivdvjvve  yi cvb à jffrds tdp  rvwdv sebr onvnqsy zvp  zuhjwiM le wmifo wiezib nec  triot qmjvr'c onrwz  memfqg srq wdaietsq vk"
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
        if 97 <= ord(c) <= 122 : #Vérifier si c'est une lettre
            alphabet[ord(c)-97][1] += round(1/len(texte),3)*100


