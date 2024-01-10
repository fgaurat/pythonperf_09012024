from Rectangle import Rectangle


class Carre(Rectangle):

    def __new__(cls,*args,**kwargs):
        print("__new__ Carre",*args,**kwargs)
        return super(Carre,cls).__new__(cls)
    
    def __init__(self, cote: int = 0):
        super().__init__(cote, cote)
        print("__init__ Carre",cote)
        self.__cote = cote

    
    @property
    def cote(self):
        return self.__cote
    
    @cote.setter
    def cote(self,cote):
        self.longueur = cote
        self.largeur = cote
        self.__cote = cote

    def __str__(self) -> str:
        return f"{__class__.__name__} {self.__cote=}"