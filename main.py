# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import colors as c
from plants import plants
from fonction import *
import csv

def main(genmax,alpha,N,L,delta,sigma,p_int):
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
    p_ext =p_int
    density=[1]
    T=0
    # on genere la grille de départ remplie des plantes de quality 1 avec alpha fixé
    g = generate_grille(L, alpha)
    while gen < genmax and density[-1] !=0:  # 
        graine=[]
        # graines dispersées + implantation
        for i in g :
            sucessBino = rd.binomial(N, alpha) #nb de graines qui seront dispersées/plantes
            g_graines1 = dispersandimplementation_fixes(
                        i,sucessBino, N, L, delta, p_int)  # graines fixées
            g_graines2 = implantation_disp(
                        sucessBino, i,L,p_ext,sigma)  # graines dispersées
            graine+=g_graines1+g_graines2
        g,nb_plt = selection(graine,L)
        T=gen  #le temps d'extinction 
        gen += 1
        density.append(nb_plt/(L*L)) #on calcule la densité des plantes dans la grille

    return density,T

def modelfigure11():
    simulation=100
    param=[[100,0,5,100,0,0.25,i] for i in np.linspace(0,1,num=10)]
    with open (f'data/figure1/sim1_gen100_N5_alpha0_L100.csv','w',newline='') as file1, open (f'data/figure1/figure11delta0.csv','w',newline='') as file2:

        #lignes pour écrire dans un fichier
        writer1=csv.writer(file1)#les données brutes
        writer2=csv.writer(file2)#on stocke les points pour le graph dans ce fichier
        writer1.writerow(['simulation','generation','rho','p_int'])
        writer2.writerow(['p_int','density'])

        for ai in param:
            m=np.zeros(simulation)
            for k in range(simulation):
                density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])
                for j in range(np.size(density)):          
                    writer1.writerow([k+1,j,density[j],ai[6]])
                    if density[-1]==0:
                        m[k]=0
                    else:
                        m[k]=(np.mean(density[int(np.size(density)/2):np.size(density)]))
            writer2.writerow([ai[6],np.mean(m)])

def modelfigure12():  #jsp comment faire
    simulation=1
    param=[[100,1,5,100,0,0.25,i] for i in np.linspace(0,1,num=10)]
    with open (f'data/figure1/sim1_gen100_N5_alpha1_L100.csv','w',newline='') as file1, open (f'data/figure1/figure12.csv','w',newline='') as file2:

        #lignes pour écrire dans un fichier
        writer1=csv.writer(file1)#les données brutes
        writer2=csv.writer(file2)#on stocke les points pour le graph dans ce fichier
        writer1.writerow(['simulation','generation','rho','p_int','sigma'])
        writer2.writerow(['p_int','density'])

        for ai in param:
            m=np.zeros(simulation)
            for k in range(simulation):
                density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])
                for j in range(np.size(density)):          
                    writer1.writerow([k+1,j,density[j],ai[6]])
                    if density[-1]==0:
                        m[k]=0
                    else:
                        m[k]=(np.mean(density[int(np.size(density)/2):np.size(density)]))
            writer2.writerow([ai[6],np.mean(m)])
        

def modelfigure2():
    simulation=1
    d,N,L,p_int=100,5,50,0.25
    with open (f'data/figure2/sim{simulation}_gen{d}_N{N}_L{L}_pint{p_int}.csv','w',newline='') as file1, open (f'data/figure2/figure2.csv','w',newline='') as file2:

        #lignes pour écrire dans un fichier
        writer1=csv.writer(file1)#les données brutes
        writer2=csv.writer(file2)#on stocke les points pour le graph dans ce fichier
        writer1.writerow(['delta','sigma/pext','simulation','generation','rho','alpha'])
        writer2.writerow(['delta','sigma/pext','rho','alpha',])

        for delta in [0,0.025,0.5]: #boucle sur les valeur de delta
            for s in [0,0.5,1]: #boucle sur les valeurs de sigma/pext
                param=[[d,i,N,L,delta,s*0.25,p_int] for i in np.linspace(0,1,num=10)]
                for ai in param: #boucle sur les valeurs de alpha
                    m=np.zeros(simulation)
                    for k in range(simulation):
                        density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])
                        for j in range(np.size(density)):          
                            writer1.writerow([delta,s,k+1,j,density[j],ai[1]])
                            if density[-1]==0:
                                m[k]=0
                            else:
                                m[k]=(np.mean(density[int(np.size(density)/2):np.size(density)])) #on fait la moyenne de la densité sur les gen/2 derniers resulats
                    writer2.writerow([delta,s,np.mean(m),ai[1]]) #on fait la moyenne sur les simulations


def modelfigure31():
    simulation=1000
    d,N,delta,sigma,p_int=500,5,0.05,0.25,0.25
    # k in 2**np.arange(2,6,1): #la taille de la grille
    param=[[d,i,N,8,delta,sigma,p_int] for i in np.linspace(0,1,num=10)]
    with open (f'data/figure3/sim{simulation}_gen{d}_N{N}_pint{p_int}.csv','w',newline='') as file1, open (f'data/figure3/figure31alpha.csv','w',newline='') as file2:

        #lignes pour écrire dans un fichier
        writer1=csv.writer(file1) #les données brutes
        writer2=csv.writer(file2) #on stocke les points pour le graph dans ce fichier
        writer1.writerow(['simulation','generation','rho','alpha'])
        writer2.writerow(['alpha','T','L'])

        for ai in param:
            m=np.zeros(simulation) #pour stocker les T
            for k in range(simulation):
                density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])
                for j in range(np.size(density)):            
                    writer1.writerow([k+1,j,density[j],ai[1]])
                    m[k]=T  #on stocke les T sur toutes les simulations
            writer2.writerow([ai[1],np.mean(m),8])      #on prend la moyenne des T



def modelfigure32():
    simulation=1000
    d,N,delta,sigma,p_int=500,5,0.05,0.25,0.25
    for j in [0,0.25,0.5,0.75,1]: #les différents alpha

        param=[[10000,j,5,i,0.05,0.25,0.25] for i in [2,10,100,500]]
        with open (f'data/figure3/pint0.25_n5_sigma0.25.csv','w',newline='') as file1, open (f'data/figure3/figure32size.csv','w',newline='') as file2:
            
            #lignes pour écrire dans un fichier
            writer1=csv.writer(file1)   #les données brutes
            writer2=csv.writer(file2)#on stocke les points pour le graph dans ce fichier
            writer1.writerow(['simulation','generation','rho','L'])
            writer2.writerow(['L','T','alpha'])
            
            for i,ai in enumerate(param):
                m=np.zeros(simulation)  #pour stocker les T
                for k in range(simulation):
                    density,T=main(ai[0],ai[1],ai[2],ai[3],ai[4],ai[5],ai[6])          
                    writer1.writerow([k+1,i,density[i],ai[3]])
                    m[k]=T  #on stocke les T sur toutes les simulations
                writer2.writerow([ai[1],np.mean(m),j])  #on prend la moyenne des T


modelfigure2()