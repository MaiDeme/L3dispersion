import numpy as np
import random
import numpy.random as rd


def implantation_disp(plante,N,inte_grille,p_ext):
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
    for i in np.arange(reproduction_plante(plante,N)): #boucle qui modélise la dispersion pour chaque graine
        x= random.randint(0, len(inte_grille)-1) #choisis aléatoirement une ligne sur la grille
        y= random.randint(0, len(inte_grille)-1) #choisis aléatoirement une colonne sur la grille
        j=rd.binomial(1, proba_installation,) #simule la proba de s'installé sur une case
        
        if j==1:
            inte_grille[x][y].append(plants(1,[x,y],plante.get_alpha)) #si la graine s'installe alors on place une instance dela class plants dans la case correspondante, il peut y avoir plusieurs plantes sur une case

    return inte_grille