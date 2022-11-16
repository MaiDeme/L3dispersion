import numpy as np
import random
import numpy.random as rd


def reproduction_plante(plante, N):
    '''
    renvoie le nombre de graines fixées pour une plante
    parametre:
    plante = une instance de la class plants
    N = nombre de graines par plante
    return
    le nombre de graines dispersées
    '''
    disp_seed = rd.binomial(N, plante.get_alpha,)
    return disp_seed
