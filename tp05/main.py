from Rectangle import Rectangle

def main():
    r = Rectangle(3,6)
    r1 = Rectangle.buildFromStr("3,6")

    print(r1)
    print(r1.get_cpt())
    print(Rectangle.get_cpt())
    # print(r1.__dict__)
    # r1.lngueur = 12
    print(r1.__dict__)
    
if __name__ == '__main__':
    main()