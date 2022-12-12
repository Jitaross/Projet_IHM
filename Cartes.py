import random as r
from PIL import Image, ImageDraw

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
        tmp = ""#variable qui contiendra le nom de la carte
        while nom_fic[i] != ".":#boucle pour récupérer le nom de la carte
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
        new_im = Image.new("RGB", (60,40), (255,255,255))#creation de l'image

        file = open(self.fichier, "r")
        if file == None:
            return 1

        ligne = file.read()
        cpt = 0 #nombre de ligne

        draw = ImageDraw.Draw(new_im)

        for i in range(60):
            if i%2:
                draw.line((i, 0, i, 40), fill = (0,0,0,0))
        for i in range(40):
            if i%2:
                draw.line((0,i,60,i), fill = (0,0,0,0))

        for i in range(len(ligne)):
            if i%30 == 0 and i != 0:
                cpt += 2
            if ligne[i] == "1":#si la case regardée est un obstacle
                if i%2:
                    x,y = (i%30)+1,cpt
                else:
                    x,y = (i%30) * 2,cpt #i%30 pour pas dépasser les 30 colonnes
                new_im.putpixel((x,y),(0,0,0))#colore le pixel a la position x,y en noir

        new_im.save("./Cartes/"+self.nom+".png", "PNG")#sauvegarde l'image en format png

        file.close()

    def test_mur(self, x, y):
        """
        fonction qui teste si la case visée est un mur(True) ou non(False)
        probleme : fonction totalement tributaire de tkinter -> essayer de trouver une solution
        """
        pass



def gencartes():
    """
    genere une liste aleatoire pour une carte
    """
    liste = ""#chaine de caratere qui contiendra la suite de 0 et de 1
    cpt = 0
    for i in range(600):
        if cpt < 120:
            tmp = r.randrange(0,6)
            if tmp == 1:
                if (i > 30) and ((liste[i - 31] == "0") and (liste[i - 29] == "0")):#permet de ne pas placer d'obstacles si le voisin du dessus gauche ou droite est un obstacle
                    liste += "1"
                    cpt += 1
                elif (i <= 30) :#pour placer un obstacle si c'est la premiere ligne
                    liste += "1"
                    cpt += 1
                else:#sinon met une case vide
                    liste += "0"
            else :
                liste += "0"
        else :
            liste += "0"

    nom = "./Cartes/Carte" + "0" + ".crt"
    file = open(nom, "w")
    file.write(liste)
    file.close()
    #print(cpt)

gencartes()
C1 = cartes()
C1.association("./Cartes/Carte0.crt")
C1.init_image()
