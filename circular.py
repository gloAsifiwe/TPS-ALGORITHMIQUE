from abc import ABCMeta, abstractclassmethod
from math import * #importer tout ce qu'il ya en math


class forme_geometrique(metaclass= abc.ABCMeta):
    @abstractclassmethod()
    def surface():
        return
    @abstractclassmethod()
    def perimetre():
        return
    
class rectangle(forme_geometrique)
    def __init__(self,H,L) :
        self.H = hauteur
        self.L = largeur
    def calcul_surface(self):
        return self.H * self.L
    def calcul_du_perimetre(self):
        return (self.L+self.H)*2
class triangle(forme_geometrique)
    def __init__(self,H,B,T) :
        self.H = hauteur
        self.B = base
        self.T= hypothenus
    def calcul_surface(self):
        return (self.H * self.B)/2
    def calcul_du_perimetre(self):
        return self.L+self.H+self.T
 class cercle(forme_geometrique)
    def __init__(self,R,D,pi) :
        self.R = rayon
        self.D = diametre
        self.pi= pi
    def calcul_surface(self):
        return  self.pi*self.R**2
    def calcul_du_perimetre(self):
        return self.L+self.H+self.T
