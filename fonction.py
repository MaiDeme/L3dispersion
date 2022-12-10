# -*- coding: utf-8 -*-
from math import sqrt
import numpy as np
from plants import plants
import random
import numpy.random as rd


def generate_grille(L, alpha):
    """
    fonction qui génère un np.array à une dimension rempli des objects 'plants'
    input: L, la longueur voulue de la grille des plantes
    output: grille, le np.array rempli de L*L élements
    """
    size = L**2
    grille = []
    for i in range(L):
        for j in range(L):
            grille.append(plants(1, (i, j), alpha))
    return grille

def liste_vide(L):
    """
    créer un tableau L**2 de liste vide.
    return
    la grille vide
    """
    grille=[]
    for i in range(L**2):
        grille.append([])
    return grille

def selection(grille,L):
    """
    selection dans chaque cases parmi la liste des graines cell qui va pousser et donner une plante
    compte aussi le nombre de plantes
    input: grille, la grille qui contient les listes des graines DEJA implanter
    ouput: g la grille avec les instances de plantes qui ont poussées et le nb de plantes

    """
    nb=0

    res= liste_vide(L)
    resfinal=[]
    for P in grille:
    
        # on choisis la graine parmi la liste
        coord=P.get_position()
        res[coord[0]*L+coord[1]].append(P)
    for i in res:
        if len(i) >1:
                resfinal.append(np.random.choice(i))
                nb+=1
        elif len(i)==1:
            resfinal.append(i[0])
            nb+=1
    return resfinal,nb

def implantation_disp(sucessBino, plante, L, real_p_ext, sigma):
    """
    remplie une liste avec les graines dispersées implantées d'une plante.
    paramètres:
    sucessBino = nombre de graines dispersées par plante
    plante = la plante mère
    L = nombre de lignes de la grille initiale
    p_ext: valeur de la proba de s'installer 

    return:
    la liste remplie des plantes (dispersées) implantées pour une seule plantes
    """
    resultat = []
    # boucle qui modélise la dispersion pour chaque graine
    for i in range(sucessBino):
        # choisis aléatoirement une ligne sur la grille
        x = random.randint(0, L-1)
        # choisis aléatoirement une colonne sur la grille
        y = random.randint(0, L-1)

        # simule la proba de s'installer sur une case    
        j = rd.binomial(1, real_p_ext)

        if j == 1:
            # si la graine s'installe alors on place une instance de la class plants dans la liste de résultat, il peut y avoir plusieurs plantes avec les même coordonnées
            resultat.append(plants(1, [x, y], plante.get_alpha()))

    return resultat


def dispersandimplementation_fixes(planteM, succesBino, L, delta, p_int):
    '''
    input: N nombre de descendants par plante
    L longueur d'un cote de la grille
    pint la probabilité d'établissement des graines fixées
    '''
    resultat=[]
    if (0 < planteM.get_position()[0] < L-1 and 0 < planteM.get_position()[1] < L-1):  #si on est au milieu de la grille
        for i in range(succesBino): #boucle sur le nombre de graines fixées
            x = planteM.get_position()[0] + \
                np.random.choice(np.array([-1, 0, 1]))
            y = planteM.get_position()[1] + \
                np.random.choice(np.array([-1, 0, 1]))
            graine = plants(planteM.get_quality(), [
                            x, y], planteM.get_alpha())
            graine.newquality(delta)
            if (rd.binomial(1, p_int*graine.get_quality()) == 1):
                resultat.append(graine)
    else: # test si on est au bord de la grille
        for i in range(succesBino):
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
            
            graine = plants(planteM.get_quality(), [
                            xfinal, yfinal], planteM.get_alpha())
            graine.newquality(delta)
            if (rd.binomial(1, p_int*graine.get_quality()) == 1):
                resultat.append(graine)
    return resultat