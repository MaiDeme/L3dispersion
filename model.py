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
    ''' la fonction qui determine blablabla
    '''
    return None

def non_dispersing():
    return None

def growth():
    return None


def generate_grille(size):
    L=size
    #grille=np.zeros((L,L))
    grille=np.random.randint(2, size=(L,L))  #pour mieux visualiser le rendu mais on devra garder juste la ligne au dessus
    #créer la grille et l'exporter
    fig,ax = plt.subplots(1, 1)
    colorarray=[[1,0,0,1 ],[1, 1, 1 ,1 ]]
    cmap = c.ListedColormap(colorarray)
    a = ax.pcolormesh(grille,edgecolors='k',linewidths=2,facecolors=['red','white'],cmap=cmap)
    ax.set_title(f"maillage {L}x{L}")

    plt.savefig('figure.png') #sauvegarder les tracés dans un .png
    plt.show()
    
    return None

def main():
    generate_grille(10)
    return None

main()