# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors as c
from plants import plants
import random
import numpy.random as rd


def affiche_grille_graines(grille):
    """
    Pour afficher la grille prise en argument mais je pense que ça sera utile que pour les test
    PAS AU POINT
    """
    L = grille.size
    fig, ax = plt.subplots(1, 1)
    colorarray = np.array([[1, 0, 0, 1], [1, 1, 1, 1]])
    cmap = c.ListedColormap(colorarray)
    a = ax.pcolormesh(grille, edgecolors='k', linewidths=2,
                      facecolors=['red', 'white'], cmap=cmap)
    ax.set_title(f"grille avec repartiiosn des graines")
    plt.show()


def affiche_grille_plantes(grille):
    """
    Pour afficher la grille prise en argument mais je pense que ça sera utile que pour les test
    PAS AU POINT
    """
    L = len(grille)
    fig, ax = plt.subplots(1, 1)
    colorarray = np.array([[1, 0, 0, 1], [1, 1, 1, 1]])
    cmap = c.ListedColormap(colorarray, 3)
    a = ax.pcolormesh(grille, edgecolors='k', linewidths=2,
                      facecolors=['red', 'white'], cmap=cmap)
    ax.set_title(f"maillage")
    plt.show()


def generate_grille(L):
    """
    fonction qui génère un np.array à deux dimensions rempli des objects 'plants'
    input: L, la longueur voulue
    output: grille, le np.array rempli
    """
    grille = np.ndarray((L, L), dtype=list)
    for i in range(L):
        for j in range(L):
            grille[i, j] = [plants(1, (i, j))]
    # grille=np.random.randint(2, size=(L,L))   #la ligne pour générer une grille random
    return grille


def selection(grille, delta):
    """
    selection dans chaque cases parmi la liste des graines cell qui va pousser et donner une plante
    input: grille, la grille qui contient les listes des graines
    ouput: g la grille avec les instances de plantes qui ont poussées

    """
    L = grille.size
    g = np.zeros((L,L))
    for i in range(L):
        for j in range(L):
            g[i][j] = np.random.choice(grille[i][j]) #on choisis la graine parmi la liste
            if g[i][j].get_quality == 1: #il faudrait trouver un test pour determiner si la graine est issu d'autofecondation
                g[i][j].quality(delta) #on applique le penalité liée à l'autofecondation
    return g


def implantation_disp(L, g, alpha, proba_installation, N):
    """
    remplie la grille avec les graines dispersées.
    paramètres:
    p : la plante (l'instance de la classe plants étudiée)
    L : la longeur de la grille
    g : une grille de taille L*L
    alpha : proportion de graines dispersées
    N : nb de graines par plantes

    return:
    la grille remplie des plantes (dispersées) implantées (liste de plantes dans chaques cases)

    """
    nb_g = int(alpha*N)  # le nombre de graines dispersées de la plante

    for i in np.arange(nb_g):  # boucle qui modélise la dispersion pour chaque graine
        # choisis aléatoirement une ligne sur la grille
        x = random.randint(0, L-1)
        # choisis aléatoirement une colonne sur la grille
        y = random.randint(0, L-1)
        # simule la proba de s'installer sur une case
        j = rd.binomial(1, proba_installation,)

        if j == 1:
            # si la graine s'installe alors on place une instance de la claas plants dans la case correspondante, il peut y avoir plusieurs 1 sur une case
            g[x][y].append(plants(1, [x, y]))

    return g
