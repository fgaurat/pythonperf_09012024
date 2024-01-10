from Rectangle import Rectangle
from Cercle import Cercle
# from RectangleSingleton import RectangleSingleton
# from Carre import Carre

# __new__ : créer l'instance
# __init__ : initialiser l'instance
# __call__ : appeler un objet comme une fonction

def main():
    # r = Carre(4)
    r = Rectangle(4,5)
    r1 = Rectangle(4,5)
    c = Cercle(14)
    c1 = Cercle(14)

    r2 = Rectangle(4,5)
    print(hex(id(r)))
    print(hex(id(r1)))
    print(hex(id(r2)))
    print(hex(id(c)))
    print(hex(id(c1)))
    print(r)
    print(r1)
    print(c)
    print(c1)
    # r1 = Rectangle(4,5)
    # r()
    # print(hex(id(r)))
    # print(hex(id(r1))) 
    # rs1 = RectangleSingleton(4,5)
    # rs2 = RectangleSingleton(43,54)
    # print(hex(id(rs1)))
    # print(hex(id(rs2)))
    # print(rs1)
    # print(rs2)

    # rs2.longueur = 1423
    # print(rs1)
    # print(rs2)
    # print(type(rs1))
    # print(type(RectangleSingleton))
if __name__ == '__main__':
    main()