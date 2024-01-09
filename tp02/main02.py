


def init():
    name = "Fred"
    l = [i for i in range(1E6)]

    def showName():
        print(name,l)
    
    # showName()
    return showName


def main():
    showName = init()
    showName() # Fred
    # None
    # Error ?
    

if __name__ == '__main__':
    main()