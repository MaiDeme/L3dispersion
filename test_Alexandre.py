import numpy as np
import random
import numpy.random as rd


alpha = float(input("Entrez la proportion de graines dispersées: "))
N = int(input("Entrez le nombre de graines par plante: "))
L = int(input("Entrez longueur de la grille: "))


class plants:
    """
    Classe d'objects à deux attribus, la qualité q entre 0 et 1 et une liste de deux entiers pour les positions des plantes dans la grille.
    """

    def __init__(self, quality, position):
        self.quality = quality
        self.position = position

    def get_position(self):
        return self.position

    def get_quality(self):
        return self.quality

    def quality(self, delta):
        self.quality = (1-delta)*self.quality


def grille_inter(L):
    """
    créer un tableau de list L*L.
    """
    g = []
    for i in np.arange(L):
        x = [[]]
        j = 0
        while j < (L-1):
            x.append([])
            j += 1
        g.append(x)
    return g


def implantation_disp(p, L, g, alpha):
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
    nb_g = int(alpha*N)  # récupère le nombre de graines dispersées de la plante

    for i in np.arange(nb_g):  # boucle qui modélisez la dispersion aléatoire
        # choisis aléatoirement une ligne sur la grille
        x = random.randint(0, L-1)
        # choisis aléatoirement une colonne sur la grille
        y = random.randint(0, L-1)
        # simule la proba de s'installé sur une case, attention la proba est fixé c'est à modifié.
        j = rd.binomial(1, 0.8,)

        if j == 1:
            # si la graine s'installe alors on place un 1 sur la case correspondante, il peut y avoir plusieurs 1 sur une case
            g[x][y].append(plants(1, [x, y]))

    return g


def generate_plants(L):
    """
    génère autant d'instance de la class plants que de case sur la grille.
    paramètre:
    L : taille de la grille

    """
    liste = []

    for i in np.arange(L):
        for j in np.arange(L):
            # ajoute à la liste l'instance de la class plants asociée à la position [i][j]
            liste.append(plants(1, [i, j]))
    return liste


print(generate_plants(L))
for e in generate_plants(L):
    print(e.get_position())


p1 = plants(1, [3, 4])

g = implantation_disp(p1, L, grille_inter(L))
print(g)
print()
for i in range(len(g)):
    for j in range(len(g[i])):
        print(g[i][j], end=' ')
    print()


# test sélection
