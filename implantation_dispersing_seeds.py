import numpy as np
import random
import numpy.random as rd


def implantation_disp(g,alpha,N,proba_installation):
    """
    produit une grille intermédiaire vide 
    remplie la grille avec les graines dispersées implantées.
    paramètres:
    g : une grille de taille L*L contenant les plantes gen(n-1)
    alpha : proportion de graines dispersées
    N: nombre de graines par plantes
    proba_installation: valeur de la proba de s'installer 

    return:
    la grille remplie des plantes (dispersées) implantées

    """  
    #créer un tableau de list L*L.
    inte_grille=[]
    for i in np.arange(len(g)):
        x=[[]]
        j=0
        while j<(L-1):
            x.append([])
            j+=1
        inte_grille.append(x) 


    #compte le nombre de plantes sur la grille 
    nb_plante=0  
    for i in np.arange(len(g)):
        for j in np.arange(len(g)):
            if g[i][j]!=[]:
                nb_plante+=1

    nb_g=int(nb_plante*alpha*N)# le nombre total de graines dispersées 

    for i in np.arange(nb_g): #boucle qui modélise la dispersion pour chaque graine
        x= random.randint(0, L-1) #choisis aléatoirement une ligne sur la grille
        y= random.randint(0, L-1) #choisis aléatoirement une colonne sur la grille
        j=rd.binomial(1, proba_installation,) #simule la proba de s'installé sur une case
        
        if j==1:
            inte_grille[x][y].append(plants(1,[x,y])) #si la graine s'installe alors on place une instance dela claas plants dans la case correspondante, il peut y avoir plusieurs 1 sur une case

    return inte_grille