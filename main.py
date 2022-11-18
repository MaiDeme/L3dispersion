# -*- coding: utf-8 -*-

from math import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *


def main():
    d = 10  # le nombre de générations
    k = 0
    alpha = 0  # proportions de graines dispersées
    N = 5  # nombre de graines
    L = 100  # taille du maillage
    delta = 0
    p_ext = 0.2
    p_int = 0.2
    density=[]
    # on genere la grille de départ remplie des plantes de quality 1 avec alpha fixé
    g = generate_grille(L, alpha)
    while k <= d:  # condition fixée pour l'instant les générations
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
                        g[i][j][0], N, g_graines, p_ext)  # graines dispersées
        g_plantes,nb_plt = selection(g_graines)
        k += 1
        density.append(nb_plt/(L*L)) #on calcule la densité des plantes dans la grille
        
    print(density)
    return density

main()



