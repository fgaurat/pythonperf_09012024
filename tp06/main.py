from Carre import Carre
from Cercle import Cercle

def main():
    c = Carre(2)
    print(c.cote)
    c.cote = 34
    print(c.surface)
    print(c)
    ce = Cercle(3)

if __name__ == '__main__':
    main()