# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *

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
        # on fait une boucle sur toute les plantes
        for i in g:
            # nb de graines qui seront dispersées/plantes
            sucessBino = rd.binomial(N, alpha)

            g_graines1 = dispersandimplementation_fixes(
                i, N-sucessBino, L, delta, p_int)  # graines non dispersées

            g_graines2 = implantation_disp(
                sucessBino, i, L, real_p_ext, sigma)  # graines dispersées

            graine += g_graines1+g_graines2

        g, nb_plt = selection(graine, L)
        T = gen  # le temps d'extinction
        gen += 1
        # on calcule la densité des plantes dans la grille
        density.append(nb_plt/(L*L))

    return density, T
