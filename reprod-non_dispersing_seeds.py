import numpy as np
import random
import numpy.random as rd
from plants import plants

# à mettre avant if (N-succesBino == 0) : break


def dispersandimplementation_fixes(planteM, succesBino, N, L, grilleD, delta, pint):
    '''
    input: N nombre de descendants par plante
    L longueur d'un cote de la grille
    pint la probabilité d'établissement des graines fixées
    '''
    if (0 < planteM.get_position()[0] < L-1 and 0 < planteM.get_position()[1] < L-1):
        for i in range(0, N-succesBino, 1):
            x = planteM.get_position()[0] + \
                np.random.choice(np.array([-1, 0, 1]))
            y = planteM.get_position()[1] + \
                np.random.choice(np.array([-1, 0, 1]))
            graine = plants(planteM.newquality(delta), [
                            x, y], planteM.get_alpha())

            if (rd.binomial(1, pint*graine.get_quality() == 1)):
                grilleD[graine.get_position()[0], graine.get_position()
                        [1]].append(graine)
    else:
        for i in range(0, N-succesBino, 1):
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

            graine = plants(planteM.newquality(delta), [
                            xfinal, yfinal], planteM.get_alpha())
            if (rd.binomial(1, pint*graine.get_quality() == 1)):
                grilleD[xfinal, yfinal].append(graine)

    return grilleD
