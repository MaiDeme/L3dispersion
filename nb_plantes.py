import numpy as np
import random
import numpy.random as rd


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
    for i in np.arange(g.size()):
        for j in np.arange(g.size()):
            if g[i][j] != []:
                nb_plants += 1
    return nb_plants
