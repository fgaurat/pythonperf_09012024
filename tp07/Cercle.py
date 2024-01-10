import math
from Singleton import Singleton

class Cercle(metaclass=Singleton):

    def __init__(self, rayon: int = 0):
        self.__rayon = rayon

    @property
    def rayon(self):
        return self.__rayon
    
    @rayon.setter
    def rayon(self,rayon):
        self.__rayon = rayon

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__rayon=}"

    @property    
    def surface(self):
        return math.pi*self.__rayon**2
