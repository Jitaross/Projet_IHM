import tkinter as tk
import test
import random
'''
creation de class pour les robots
'''
class robot:
    '''
    cette fonction est le constructeur par parametre qui permet d'initialiser les robots
    '''
    def __init__(self,nom,fichier,x,y,energie):
        self.nom=nom #nom du robot
        self.fichier=fichier #fichier qui contient toute les instructions du robot
        #position du robot sur la carte
        self.pos_x=x #abscisse
        self.pos_y=y
        self.energie=energie

    '''
    fonction qui fait les déplacements aléatoire du robot
    '''

    def direction(self,tab,x,y):

        continuer=True
        x1,y1 = x,y #sauvegarder les valeurs de départ
        dir = {0:(0,-1), 1:(0,1), 2:(1,0), 3:(-1,0)}
        while (continuer):
            rand=random.randrange(0,4) #definir la case au hasard
            x,y = x1 + dir[rand][0], y1 + dir[rand][1] #bouger le robot
            continuer = test.testmur(tab,x,y) #test s'il y a un mur
            #print(x,y,continuer)
        #nouvelle positiposeon du robot
        self.pos_x=x
        self.pos_y=y
        #print(self.pos_x)
        #print(self.pos_y)

     '''
    fonction qui place la mine sur un case
    '''

    def placer_mine(x,y):
        mine = #classmine



    '''
    fonction qui determine la postion de la mine sur 1 des 4 cases
    '''

    def mine(self,tab,x,y):
        if(self.energie<10): #si le robot n'a pas assez d'energie
            return 1
        continuer = True
        x1,y1 = x,y
        dir = {0:(0,-1), 1:(0,1), 2:(1,0), 3:(-1,0)}
        while (continuer):
            rand=random.randrange(0,4) #definir la case au hasard
            x,y = x1 + dir[rand][0], y1 + dir[rand][1] #bouger le robot
            continuer = test.testmur(tab,x,y)
        placer_mine(x,y)
        return 0






''''
    def commande (self,nomFichier):

        nomFichier=open(nomFichier,"r")#ouvre le fichier
        l=nomFichier.readlines()[1::] #self.pos_x=x lis le fichier à partir de la deuxième ligne
        tmp=[]
        commande=[]
        for ligne in l: #prend les commandes
            tmp=tmp+[ligne]

        for i in range (len(tmp)):
            commande=commande+[tmp[i].strip("\n")] #enlène \n

        #print(commande)
        #print(len(commande))
        for i in range(len(commande)):
            if (commande[i]=="MI"):
                print("MI")
            if(commande[i]=="AL"):self.pos_x=x
                print("AL")
            if (commande[i]=="DD"):
                print("DD")
            if(commande[i]=="IN"):
                print("IN")
            if(commande[li]=="PS"):
                print("PS")
            if(commande[i]=="FT"):
                print("FT")
            if(commande[i]=="TT"):
                print("TT")
            if(commande[i]=="TV"):
                print("TV")
            if(commande[i]=="TH"):
                print("TH")
'''





def gen_tab():
    tab=[]
    tab=[random.randint(0,1) for i in range(600)]
    return tab

R1=robot("R1","tot.txt",0,0,200)
#print(R1.nom)
#print(R1.fichier)
#print(R1.verification("tot.txt"))
#R1.commande("tot.txt")

R1.direction(gen_tab(),0,0)
