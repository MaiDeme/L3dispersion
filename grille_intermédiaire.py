import numpy as np
import random
import numpy.random as rd



def grille_inter(grille_gen_avant): 
    """
    créer un tableau de list L*L.
    parametre
    grille_gen_avant = numpy array 2d contenant des listes avec les plantes de la gen précedente
    return
    la grille intermédiaire même taille que grille_gen_avant mais vide
    """        
    #créer un tableau de list L*L.
    inte_grille=[]
    for i in np.arange(g.size()):
        x=[[]]
        j=0
        while j<(g.size()-1):
            x.append([])
            j+=1
        inte_grille.append(x)
    return inte_grille