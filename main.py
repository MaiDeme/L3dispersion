# -*- coding: utf-8 -*-

from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *


def main():
    d=5 #le nombre de générations
    i=0
    alpha=0     #proportions de graines dispersées
    N=3         #nombre de graines
    L=10        #taille du maillage
    delta=0
    p_ext=0.2  
    g1=generate_grille(5) #on genere la grille de départ remplie des plantes de quality 1
    while i <d: #condition fixée pour l'instant le temps de comprendre tout
        g2=np.zeros((5,5)) #on genre  une grille vide pour y mettre les graines
        #dispersion (pour l'instant juste les graines dispersées) +implantation
        g2=implantation_disp(L,g2,alpha,p_ext,N)
        #donc la on a la grille avec les graines dipersées ET implantés
        g3=np.empty((L,L))
        #dispersion graines fixées
        g=np.empty((L,L))
        for i in range (L):
            for j in range(L):
                g[i][j]=g2[i][j]+g3[i][j]  #on concatène les listes
                

   g=selection(g)

    return g


main()
