

class Rectangle:
    """
    La class Rectangle
    """

    def __init__(self,longueur:int=0,largeur:int=0):
        self.__longueur = longueur
        self.__largeur = largeur

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