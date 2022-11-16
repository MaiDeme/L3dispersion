import numpy as np
import random
import numpy.random as rd

#à mettre avant if (N-succesBino == 0) : break

def dispersion_fixes(plante,succesBino,grilleDescendants,N,L) :
  
 """ N nombre de descendants par plante
 L longueur d'un cote de la grille"""

  for i in range (0,N-succesBino,1) : 
    
    if( 0 < plante.get_position()[0] < L-1 and 0 < plante.get_position()[1] < L-1) :
      x = np.random.choice(np.array([-1, 0, 1]))
      y = np.random.choice(np.array([-1, 0, 1]))
      plante.newposition([x, y])
      
    
    if(plante.get_position()[0] == 0) :
      x = np.random.choice(np.array([0, 1]))
      plante.newposition([x,plante.get_position()[1]])
      
    elif(plante.get_position()[0] == L-1) :
      x = np.random.choice(np.array([-1, 0]))
      plante.newposition([x,plante.get_position()[1]])
    
    if(plante.get_position()[1] == 0) :
      y = np.random.choice(np.array([0, 1]))
      plante.newposition([plante.get_position()[0],y])
      
    elif(plante.get_position()[1] == L-1) :
      y = np.random.choice(np.array([-1, 0]))
      plante.newposition([plante.get_position()[0],y])
      
    
