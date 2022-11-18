# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as c
from plants import plants
import random
import numpy.random as rd


def generate_grille(L, alpha):
    """
    fonction qui génère un np.array à deux dimensions rempli des objects 'plants'
    input: L, la longueur voulue
    output: grille, le np.array rempli
    """
    grille = np.ndarray((L, L), dtype=list)
    for i in range(L):
        for j in range(L):
            grille[i, j] = [plants(1, (i, j), alpha)]
    # grille=np.random.randint(2, size=(L,L))   #la ligne pour générer une grille random
    return grille


def selection(grille):
    """
    selection dans chaque cases parmi la liste des graines cell qui va pousser et donner une plante
    compte aussi le nombre de plantes
    input: grille, la grille qui contient les listes des graines DEJA implanter
    ouput: g la grille avec les instances de plantes qui ont poussées et le nb de plantes

    """
    nb=0
    L = np.size(grille,0)
    g = np.empty((L, L),dtype=list)
    for i in range(L):
        for j in range(L):
            # on choisis la graine parmi la liste
            if grille[i][j] != []:
                g[i][j] = [np.random.choice(grille[i][j])]
                nb+=1
            else:
                g[i][j] = []
    return g,nb


def reproduction_plante(plante, N):
    '''
    renvoie le nombre de graines fixées pour une plante
    parametre:
    plante = une instance de la class plants
    N = nombre de graines par plante
    return
    le nombre de graines dispersées
    '''
    disp_seed = rd.binomial(N, plante.get_alpha())
    return disp_seed


def implantation_disp(plante, N, inte_grille, p_ext):
    """
    remplie la grille intermédiaire avec les graines dispersées implantées d'une plante.
    paramètres:
    plante = la plante mère
    N = nombre de graines totales par plantes
    inte_grille = grille intermédiaire
    p_ext: valeur de la proba de s'installer 

    return:
    la grille remplie des plantes (dispersées) implantées pour une seule plantes
    """
    for i in np.arange(reproduction_plante(plante, N)):  # boucle qui modélise la dispersion pour chaque graine
        # choisis aléatoirement une ligne sur la grille
        x = random.randint(0, len(inte_grille)-1)
        # choisis aléatoirement une colonne sur la grille
        y = random.randint(0, len(inte_grille)-1)
        # simule la proba de s'installer sur une case
        j = rd.binomial(1, p_ext)

        if j == 1:
            # si la graine s'installe alors on place une instance dela class plants dans la case correspondante, il peut y avoir plusieurs plantes sur une case
            inte_grille[x][y].append(plants(1, [x, y], plante.get_alpha))

    return inte_grille


def grille_vide(L):
    """
    créer un tableau LxL de liste vide.
    parametre
    L la taille du tableau LxL
    return
    la grille intermédiaire
    """
    grille = np.ndarray((L, L), dtype=list)
    for i in range(L):
        for j in range(L):
            grille[i, j] = []
    return grille


def nb_plants(g):
    '''
    compte le nombre de plantes sur la grille
    parametre
    grille= numpy array 2d de listes de plantes
    return
    le nombre de plants
    '''
    # compte le nombre de plantes sur la grille
    nb_plants = 0
    for i in np.arange(np.size(g, 0)):
        for j in np.arange(np.size(g, 0)):
            if g[i][j] != []:
                nb_plants += 1
    return nb_plants


def dispersandimplementation_fixes(planteM, succesBino, N, L, grilleD, delta, p_int):
    '''
    input: N nombre de descendants par plante
    L longueur d'un cote de la grille
    pint la probabilité d'établissement des graines fixées
    '''
    if (0 < planteM.get_position()[0] < L-1 and 0 < planteM.get_position()[1] < L-1):
        for i in range(0, N-succesBino, 1):
            x = planteM.get_position()[0] + \
                np.random.choice(np.array([-1, 0, 1]))
            y = planteM.get_position()[1] + \
                np.random.choice(np.array([-1, 0, 1]))
            planteM.newquality(delta)
            graine = plants(planteM.get_quality(), [
                            x, y], planteM.get_alpha())

            if (rd.binomial(1, p_int*graine.get_quality()) == 1):
                grilleD[graine.get_position()[0], graine.get_position()
                        [1]].append(graine)
    else:
        for i in range(0, N-succesBino, 1):
            xfinal = planteM.get_position()[0]
            yfinal = planteM.get_position()[1]

            if (planteM.get_position()[0] == 0):
                xfinal += np.random.choice(np.array([0, 1]))

            elif (planteM.get_position()[0] == L-1):
                xfinal += np.random.choice(np.array([-1, 0]))

            if (planteM.get_position()[1] == 0):
                yfinal += np.random.choice(np.array([0, 1]))

            elif (planteM.get_position()[1] == L-1):
                yfinal += np.random.choice(np.array([-1, 0]))

            planteM.newquality(delta)
            graine = plants(planteM.get_quality(), [
                            xfinal, yfinal], planteM.get_alpha())
            if (rd.binomial(1, p_int*graine.get_quality()) == 1):
                grilleD[xfinal, yfinal].append(graine)

    return grilleD