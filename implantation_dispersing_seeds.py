import numpy as np
import random
import numpy.random as rd


def grille_intermédiaire(L): 
    """
    créer un tableau de list L*L.
    """        
    g=[]
    for i in np.arange(L):
        x=[[]]
        j=0
        while j<(L-1):
            x.append([])
            j+=1
        g.append(x)
    return g



def implantation_disp(p,L,g,alpha,proba_installation):
    """
    remplie la grille avec les graines dispersées.
    paramètres:
    p : la plante (l'instance de la classe plants étudiée)
    L : la longeur de la grille
    g : une grille de taille L*L
    alpha : proportion de graines dispersées

    return:
    la grille remplie des plantes (dispersées) implantées

    """        
    nb_g=int(alpha*N)# le nombre de graines dispersées de la plante

    for i in np.arange(nb_g): #boucle qui modélise la dispersion pour chaque graine
        x= random.randint(0, L-1) #choisis aléatoirement une ligne sur la grille
        y= random.randint(0, L-1) #choisis aléatoirement une colonne sur la grille
        j=rd.binomial(1, proba_installation,) #simule la proba de s'installé sur une case
        
        if j==1:
            g[x][y].append(plants(1,[x,y])) #si la graine s'installe alors on place une instance dela claas plants dans la case correspondante, il peut y avoir plusieurs 1 sur une case

    return g