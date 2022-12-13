import tkinter as tk
import random
'''
class de creation de mine
'''
class mine:
    def __init__(self,couleur):
            '''
            cette fonction est le constructeur par parametre qui permet d'initialiser les robots
            '''
            #emplacement de la mine
            self.x = 0
            self.y = 0
            self.couleur = couleur

            '''
            fonction qui place une mine sur la carte
            '''
    def creation (self,#canvas ?):
        #poser la mine sur le canvas
