import ast
from ICalcGeo import ICalcGeo


class Rectangle(ICalcGeo):
    """
    La class Rectangle
    """
    __cpt = 0

    __slots__=['__longueur','__largeur']

    def __init__(self,longueur:int=0,largeur:int=0):
        self.__longueur = longueur
        self.__largeur = largeur
        Rectangle.__cpt+=1

    @classmethod
    def buildFromStr(cls,value):
        # longueur,largeur = [int(i) for i in value.split(',')]
        longueur,largeur = ast.literal_eval(value)
        return cls(longueur,largeur)

    @staticmethod
    def get_cpt():
        return Rectangle.__cpt



    @property
    def longueur(self):
        return self.__longueur
    @property
    def largeur(self):
        return self.__largeur

    @longueur.setter
    def longueur(self,longueur):
        self.__longueur = longueur
    
    @largeur.setter
    def largeur(self,largeur):
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__longueur=},{self.__largeur=}"
    
    # if r1 == r2:
    # if r1.__eq__(r2):
    # def __eq__(self,obj):
    #     return self.__longueur == obj.__longueur and self.__largeur == obj.__largeur 

    def __eq__(self, __value: object) -> bool:
        return self.__longueur == __value.__longueur and self.__largeur == __value.__largeur 