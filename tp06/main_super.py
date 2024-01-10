class A:
    def __init__(self) -> None:
        print("__init__ A")

    def show(self):
        print('A')

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print("__init__ B")

    def show(self):
        print('B')


class C(A):
    def __init__(self) -> None:
        super().__init__()
        print("__init__ C")

    def show(self):
        print('C')


class D(B,C):
    def __init__(self) -> None:
        super(C,self).__init__()
        print("__init__ D")

    def show(self):
        super(B,self).show()
        print('D')




def main():
    d =D()
    d.show()
    print(D.mro())

    
    # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
    # [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

if __name__ == '__main__':
    main()