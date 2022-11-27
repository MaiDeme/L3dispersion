# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *
import csv


def main(d,alpha,N,L,delta,sigma,p_int):
    """
    #param
    d pour limiter le nb de generation
    alpha la proportion de graine dispersées
    N nb de graines
    L taille du maillage
    delta
    p_int

    """
    k = 0
    p_ext =p_int
    density=[1]
    T=0
    # on genere la grille de départ remplie des plantes de quality 1 avec alpha fixé
    g = generate_grille(L, alpha)
    while k < d and density[-1] !=0:  # condition fixée pour l'instant les générations
        # on genere  une grille vide pour y mettre les graines
        g_graines = grille_vide(L)
        # graines dispersées + implantation
        for i in range(L):
            for j in range(L):
                if g[i][j] != []:
                    sucessBino = rd.binomial(N, alpha)
                    g_graines = dispersandimplementation_fixes(
                        g[i][j][0], 1-sucessBino, N, L, g_graines, delta, p_int)  # graines fixées
                    g_graines = implantation_disp(
                        sucessBino,g[i][j][0], N, g_graines, p_ext,sigma)  # graines dispersées
        g,nb_plt = selection(g_graines)
        T=k  #le temps d'extinction 
        k += 1
        density.append(nb_plt/(L*L)) #on calcule la densité des plantes dans la grille
           
    return density,T

with open (f'data/data_simulation_N100_alpha0_L50.csv','w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['simulation','generation','rho','p_int'])
    param=[[100,0,5,100,0,0.25,0.5],[100,0,5,100,0,0.25,0.9]]
    for i in range(len(param)):
        density,T=main(param[i][0],param[i][1],param[i][2],param[i][3],param[i][4],param[i][5],param[i][6]) 
        for j in range(np.size(density)):          
            writer.writerow([i+1,j,density[j],param[i][6]])






