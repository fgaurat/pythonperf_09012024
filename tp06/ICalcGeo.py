from abc import ABCMeta,abstractmethod
# Abstract Base Class

class ICalcGeo(metaclass=ABCMeta):


    @property
    @abstractmethod
    def surface(self):
        pass