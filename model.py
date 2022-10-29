# -*- coding: utf-8 -*-

from math import *
from random import *
import matplotlib.pyplot as plt 
import numpy as np
from PIL import Image
import matplotlib.image as mpimg
from matplotlib import colors as c
from plants import plants

##dispersing rules
def dispersing():
    return None

def non_dispersing():
    return None

def growth():
    return None


def affiche_grille(grille):
    """
    Pour afficher la grille prise en argument mais je pense que ça sera utile que pour les test
    """
    L=grille.size
    fig,ax = plt.subplots(1, 1)
    colorarray=[[1,0,0,1 ],[1, 1, 1 ,1 ]]
    cmap = c.ListedColormap(colorarray)
    a = ax.pcolormesh(grille,edgecolors='k',linewidths=2,facecolors=['red','white'],cmap=cmap)
    ax.set_title(f"maillage")
    plt.show()


def generate_grille(L):
    """
    fonction qui génère un np.array à deux dimensions rempli des objects 'plants'
    input: L, la longueur voulue
    output: grille, le np.array rempli
    """
    grille=np.ndarray((L,L),dtype=plants)
    for i in range(L):
        for j in range(L):
            grille[i,j]=plants(1,(i,j))
    #grille=np.random.randint(2, size=(L,L))   #la ligne pour générer une grille random
    return grille

print(generate_grille(10))
