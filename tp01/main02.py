import copy 

def main():
    l = [10,20,30,40,50] 
    l2 = l[1:4] # l[1:4[
    print(l2)
    print(l[-1]) # le dernier
    print(l[0:3])
    print(l[:3])
    print(l[3:])
    l2 = l[:]
    l[0] = 1000
    print(50*'-')
    print(l)
    print(l2)
    print(50*'-')

    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90],
    ]
    l2 = copy.deepcopy(l)
    l[0][0] = 1000

    print(l)
    print(l2)
if __name__ == '__main__':
    main()