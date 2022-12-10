# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *
import csv


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


def modelfigure11():
    simulation = 1
    param = [[100, 0, 5, 100, 0, 0.25, i] for i in np.linspace(0, 1, num=10)]
    with open(f'data/figure1/sim1_gen100_N5_alpha0_L100.csv', 'w', newline='') as file1, open(f'data/figure1/figure11delta0.csv', 'w', newline='') as file2:

        # lignes pour écrire dans un fichier
        writer1 = csv.writer(file1)  # les données brutes
        # on stocke les points pour le graph dans ce fichier
        writer2 = csv.writer(file2)
        writer1.writerow(['simulation', 'generation', 'rho', 'p_int'])
        writer2.writerow(['p_int', 'density'])

        for ai in param:
            m = np.zeros(simulation)
            for k in range(simulation):
                density, T = main(ai[0], ai[1], ai[2],
                                  ai[3], ai[4], ai[5], ai[6])
                for j in range(np.size(density)):
                    writer1.writerow([k+1, j, density[j], ai[6]])
                    if density[-1] == 0:
                        m[k] = 0
                    else:
                        m[k] = (
                            np.mean(density[int(np.size(density)/2):np.size(density)]))
            writer2.writerow([ai[6], np.mean(m)])


def modelfigure12():  # jsp comment faire
    simulation = 1
    param = [[100, 1, 5, 100, 0, 0.25, i] for i in np.linspace(0, 1, num=10)]
    with open(f'data/figure1/sim1_gen100_N5_alpha1_L100.csv', 'w', newline='') as file1, open(f'data/figure1/figure12.csv', 'w', newline='') as file2:

        # lignes pour écrire dans un fichier
        writer1 = csv.writer(file1)  # les données brutes
        # on stocke les points pour le graph dans ce fichier
        writer2 = csv.writer(file2)
        writer1.writerow(['simulation', 'generation', 'rho', 'p_int', 'sigma'])
        writer2.writerow(['p_int', 'density'])

        for ai in param:
            m = np.zeros(simulation)
            for k in range(simulation):
                density, T = main(ai[0], ai[1], ai[2],
                                  ai[3], ai[4], ai[5], ai[6])
                for j in range(np.size(density)):
                    writer1.writerow([k+1, j, density[j], ai[6]])
                    if density[-1] == 0:
                        m[k] = 0
                    else:
                        m[k] = (
                            np.mean(density[int(np.size(density)/2):np.size(density)]))
            writer2.writerow([ai[6], np.mean(m)])


def modelfigure2():
    simulation = 1
    d, N, L, p_int = 100, 5, 50, 0.25
    with open(f'data/figure2/sim{simulation}_gen{d}_N{N}_L{L}_pint{p_int}.csv', 'w', newline='') as file1, open(f'data/figure2/figure2.csv', 'w', newline='') as file2:

        # lignes pour écrire dans un fichier
        writer1 = csv.writer(file1)  # les données brutes
        # on stocke les points pour le graph dans ce fichier
        writer2 = csv.writer(file2)
        writer1.writerow(['delta', 'sigma/pext', 'simulation',
                          'generation', 'rho', 'alpha'])
        writer2.writerow(['delta', 'sigma/pext', 'rho', 'alpha', ])

        for delta in [0, 0.025, 0.5]:  # boucle sur les valeur de delta
            for s in [0, 0.5, 1]:  # boucle sur les valeurs de sigma/pext
                param = [[d, i, N, L, delta, s*0.25, p_int]
                         for i in np.linspace(0, 1, num=10)]
                for ai in param:  # boucle sur les valeurs de alpha
                    m = np.zeros(simulation)
                    for k in range(simulation):
                        density, T = main(
                            ai[0], ai[1], ai[2], ai[3], ai[4], ai[5], ai[6])
                        for j in range(np.size(density)):
                            writer1.writerow(
                                [delta, s, k+1, j, density[j], ai[1]])
                            if density[-1] == 0:
                                m[k] = 0
                            else:
                                # on fait la moyenne de la densité sur les gen/2 derniers resulats
                                m[k] = (
                                    np.mean(density[int(np.size(density)/2):np.size(density)]))
                    # on fait la moyenne sur les simulations
                    writer2.writerow([delta, s, np.mean(m), ai[1]])


def modelfigure31():
    simulation = 10
    d, N, delta, sigma, p_int = 1000, 5, 0.05, 0.25, 0.25
    # for k in 2**np.arange(2,2,1): #la taille de la grille
    param = [[d, i, N, 16, delta, sigma, p_int]
             for i in np.linspace(0, 1, num=10)]
    with open(f'data/figure3/1sim{simulation}_gen{d}_N{N}_pint{p_int}.csv', 'w', newline='') as file1, open(f'data/figure3/figure1sim{simulation}_gen{d}_N{N}_pint{p_int}.csv', 'w', newline='') as file2:

        # lignes pour écrire dans un fichier
        writer1 = csv.writer(file1)  # les données brutes
        # on stocke les points pour le graph dans ce fichier
        writer2 = csv.writer(file2)
        writer1.writerow(['simulation', 'generation', 'rho', 'alpha'])
        writer2.writerow(['alpha', 'T', 'L'])

        for ai in param:
            m = np.zeros(simulation)  # pour stocker les T
            for k in range(simulation):
                density, T = main(ai[0], ai[1], ai[2],
                                  ai[3], ai[4], ai[5], ai[6])
                for j in range(np.size(density)):
                    writer1.writerow([k+1, j, density[j], ai[1]])
                    m[k] = T  # on stocke les T sur toutes les simulations
            # on prend la moyenne des T
            writer2.writerow([ai[1], np.mean(m), ai[3]])


def modelfigure32():
    simulation = 20
    d, N, delta, sigma, p_int = 100, 5, 0.05, 0.25, 0.25
    param = [[d, 0, N, i, delta, sigma, p_int]
             for i in [2,10,50,100,200]]
    with open(f'data/figure3/2sim{simulation}_gen{d}_N{N}_pint{p_int}.csv', 'w', newline='') as file1, open(f'data/figure3/figure2sim{simulation}_gen{d}_N{N}_pint{p_int}.csv', 'w', newline='') as file2:

        # lignes pour écrire dans un fichier
        writer1 = csv.writer(file1)  # les données brutes
        # on stocke les points pour le graph dans ce fichier
        writer2 = csv.writer(file2)
        writer1.writerow(['simulation', 'generation', 'rho', 'L'])
        writer2.writerow(['L', 'T', 'alpha'])

        for ai in param:
            m = np.zeros(simulation)  # pour stocker les T
            for k in range(simulation):
                density, T = main(ai[0], ai[1], ai[2],
                                  ai[3], ai[4], ai[5], ai[6])
                for j in range(np.size(density)):
                    writer1.writerow([k+1, j, density[j], ai[3]])
                    m[k] = T  # on stocke les T sur toutes les simulations
            # on prend la moyenne des T
            writer2.writerow([ai[3], np.mean(m), ai[1]])
modelfigure31()
