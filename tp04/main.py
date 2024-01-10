from Rectangle import Rectangle
from DataRectangle import DataRectangle


def main():
    r = Rectangle(2,3)
    
    print(r.longueur)
    # print(r.get_longueur())# 2
    r.longueur = 12
    # print(r.get_longueur())# 12
    print(r.surface)# 12

    s = str(r)
    print(s)
    r1 = Rectangle(2,3)
    r2 = Rectangle(2,3)
    
    if r1 == r2:
        print("ok")
    else:
        print("ko")

    print(50*'-')
    d = DataRectangle(3,6)
    d1 = DataRectangle(3,6)
    print(d)
    print(d==d1)

if __name__ == '__main__':
    main()