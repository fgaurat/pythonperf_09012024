import sys
# import malib


def main():
    # a ="toto" # immutable
    # print(a)
    # print(hex(id(a)))
    # a = "tutu"
    # print(a)
    # print(hex(id(a)))
    
    # print(50*'-')
    # a = 2
    # b =2
    # c = 2
    # print(a)
    # print(hex(id(a)))
    # print(hex(id(b)))
    # print(hex(id(c)))
    # a = 3
    # print(a)
    # print(hex(id(a)))
    a = 3
    print(sys.getrefcount(3))
    b = 3
    print(sys.getrefcount(3))

if __name__ == '__main__':
    main()