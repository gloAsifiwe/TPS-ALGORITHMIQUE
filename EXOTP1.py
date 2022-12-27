from abc import ABCMeta,abstractmethod
from math import * #importer tout ce qu'il ya en math


class forme_geometrique(metaclass= ABCMeta):
    @abstractmethod
    def surface():
        return
    def perimetre():
        return
    
class rect (forme_geometrique):
    def __init__(self,H,L) :
        self.H = H
        self.L = L
    def calcul_surface(self):
        return self.H * self.L
    def calcul_du_perimetre(self):
        return (self.L+self.H)*2
class triangle(forme_geometrique):
    def __init__(self,H,B,T) :
        self.H = H
        self.B = B
        self.T= T
    def calcul_surface(self):
        return (self.H * self.B)/2
    def calcul_du_perimetre(self):
        return self.L+self.H+self.T
    
class cercle(forme_geometrique):
      def __init__(self,R,D,pi) :
        self.R = R
        self.D = D
        self.pi= pi
      def calcul_surface(self):
        return self.pi * self.R**2
      def calcul_du_perimetre(self):
        return self.R*2*self.pi
    