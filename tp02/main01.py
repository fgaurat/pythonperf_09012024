import monmodule

ga = 2

def main():
    global ga
    ga = 1412
    print("ga",ga)
    if True:
        a = 2
        print(a)
    


if __name__ == '__main__':
    main()
    print(ga)