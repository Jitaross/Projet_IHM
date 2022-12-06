import random as r
from PIL import Image

class cartes:
    """
    classe qui initialise une carte en fonction d'un fichier
    """

    def __init__(self):
        self.nom = ""
        self.fichier = ""

    def association(self, nom_fic):
        """
        Fonction qui associe une instance de la classe carte a un fichier en vérifiant
        que le fichier respecte les consignes
        """
        file = open(nom_fic, "r")
        if file == None:
            return 3

        cpt = [0,0] #compteur du nombre d'obstacles
        ligne = file.read()

        for j in range(len(ligne)):
            if ligne[j] == "0":#si c'est une case vide
                cpt[0] += 1

            elif ligne[j] == "1":#si c'est un obstacle
                cpt[0] += 1
                cpt[1] += 1;

        if cpt[0] > 600:#si il y a plus de cases que 600 (30*20)
            file.close()
            return 2
        elif cpt[1] > 120:#Si le nombre d'obstacles est supérieur a 20% de 600 (30*20)
            file.close()
            return 1

        self.fichier = nom_fic

        i = 1
        tmp = "" #variable qui contiendra le nom de la carte
        while nom_fic[i] != "." or nom_fic[i] == "]":#boucle pour récupérer le nom de la carte
            if nom_fic[i] != "/": #pour pas récupérer le chemin comme nom
                tmp += nom_fic[i]
                i += 1
            else :
                tmp = ""
                i += 1;

        self.nom = tmp

        file.close()

    def init_image(self):
        """
        Fonction créant une image à partir d'une carte initialisée par un fichier
        """
        new_im = Image.new("RGB", (30,20), (255,255,255))#creation de l'image

        file = open(self.fichier, "r")
        if file == None:
            return 1

        ligne = file.read()
        cpt = 0 #nombre de ligne

        for i in range(len(ligne)):
            if i%30 == 0:
                cpt += 1
            if ligne[i] == "1":#si la case regardée est un obstacle
                x,y = i%30,cpt #i%30 pour pas dépasser les 30 colonnes
                new_im.putpixel((x,y),(0,0,0))#colore le pixel a la position x,y en noir

        new_im.save("./Cartes/"+self.nom+".png", "PNG")#sauvegarde l'image en format png

        file.close()



def gencartes():
    """
    genere une liste aleatoire pour une carte
    """
    liste = ""
    cpt = 0
    for i in range(600):
        if cpt < 120:
            tmp = r.randrange(0,2)
            if tmp == 1:
                liste += str(tmp)
                cpt += 1
            else :
                liste += str(tmp)
        else :
            liste += "0"

    file = open("./Cartes/test.crt", "w")
    liste = liste
    file.write(liste)
    file.close()


gencartes()
C1 = cartes()
C1.association("./Cartes/test.crt")
C1.init_image()
