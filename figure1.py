# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *
import csv
import matplotlib.pyplot as plt          # librairie graphique
def main(genmax, alpha, N, L, delta, sigma, p_int):
    """
    #param
    genmax pour limiter le nb de generation
    alpha la proportion de graine dispersées
    N nb de graines
    L taille du maillage
    delta
    p_int

    """
    gen = 0
    p_ext = p_int
    density = [1]
    T = 0
    # on genere la grille de départ remplie des plantes de quality 1 avec alpha fixé
    g = generate_grille(L, alpha)

    # conditions pour s'arréter en cas d'extinction ou pour éviter les boucles infinies
    while gen < genmax and density[-1] != 0:
        graine = []
        real_p_ext = random.uniform(p_ext-sigma, p_ext+sigma)
        #on fait une boucle sur toute les plantes
        for i in g:
            # nb de graines qui seront dispersées/plantes
            sucessBino = rd.binomial(N, alpha)
            
            g_graines1 = dispersandimplementation_fixes(
                i,N-sucessBino, L, delta, p_int)  # graines non dispersées

            g_graines2 = implantation_disp(
                sucessBino, i, L,real_p_ext, sigma)  # graines dispersées

            graine += g_graines1+g_graines2
            
        g, nb_plt = selection(graine, L)
        T = gen  # le temps d'extinction
        gen += 1
        # on calcule la densité des plantes dans la grille
        density.append(nb_plt/(L*L))

    return density, T



fig, ax = plt.subplots()
ax.grid()
xx=np.linspace(0,1,10)



for L in [8,16,32]:
    
    y1=[]
    for alpha in xx:
        i=0
        x=[]
        
        while i !=100:
            
            d,T =main(10000,alpha,5,L,0.05,0.25,0.25)
            x.append(T)
            i+=1   
        y=np.mean(x)
        
        ax.scatter(alpha,y,color='red') 
        
        y1.append(y)
        
        x=[]
    ax.plot(xx,y1,label=f'L={L}')
ax.legend()

ax.set_xlabel("Dispersal fraction α")
ax.set_xlim(0,1)
ax.set_ylabel("Mean extinction time T")
ax.set_yscale('log')
plt.show()