# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:55:41 2022

@author: maiwe
"""
alpha = float(input("Entrez la proportion de graines dispersées: "))
N = int(input("Entrez le nombre de graines par plante: "))
L = int(input("Entrez longueur de la grille: "))


class plants:
    """
    Classe d'objects à deux attribus, la qualité q entre 0 et 1 et un couple d'entiers pour les positions des plantes dans la grille.
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

    def position(self, newposition):
        self.position = newposition

    def dispersing(self,):
        return alpha*N
