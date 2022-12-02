# -*- coding: utf-8 -*-

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
        graine=[]
        # graines dispersées + implantation
        for i in g :
            sucessBino = rd.binomial(N, alpha)
            g_graines1 = dispersandimplementation_fixes(
                        i,sucessBino, N, L, delta, p_int)  # graines fixées
            g_graines2 = implantation_disp(
                        sucessBino, i,L,p_ext,sigma)  # graines dispersées
            graine+=g_graines1+g_graines2

        g,nb_plt = selection(graine,L)
        T=k  #le temps d'extinction 
        k += 1
        density.append(nb_plt/(L*L)) #on calcule la densité des plantes dans la grille

    return density,T

simulation=20
with open (f'data/sim_gen10_N5_alpha0_L10.csv','w',newline='') as file1, open (f'data/figure3alpha0delta0.csv','w',newline='') as file2:
    writer1=csv.writer(file1)
    writer2=csv.writer(file2)
    writer1.writerow(['simulation','generation','rho','p_int'])
    writer2.writerow(['p_int','density'])
    param=[[1000,0,5,100,0,0.25,i] for i in np.linspace(0,1,num=10)]
    for i,ai in enumerate(param):
        m=np.zeros(simulation)
        for k in range(simulation):
            density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])
            for j in range(np.size(density)):          
                writer1.writerow([k+1,j,density[j],ai[6]])
                m[k]=(np.mean(density[int(np.size(density)/2):np.size(density)]))
        writer2.writerow([[ai[6]],np.mean(m)])
