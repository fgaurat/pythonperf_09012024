
def add(*l): # emballage
    print(l)
    r = 0
    for i in l:
        r+=i
    return r

def mult2(l):
    # r =[]
    # for i in l:
    #     r.append(i*2)
    r = [i*2 for i in l]
    return r


def f():
    return 12,45

def map_mult_2(i):
    return i*2

def hello(**info):
    print(info)

# def hello2(firstName,name,/): # positional only
def hello2(*,firstName,name): # keywords only
    print(firstName,name)

def main():
    l = [10,20,30]
    r = add(*l) # déballage
    print(r) # 60
    
    r = add(10,20,30)
    print(r) # 60

    print(50*'-')
    l = [10,20,30,40,50]
    a,b,c,d,e = l    
    print(a,b)
    a,b,*_ = l
    print(a,b)
    print(_)

    a,b = f()
    s =1,
    print(s)
    print(50*'-')
    l = [10,20,30]

    m = mult2(l) #
    print(m) # [20,40,60]
    # function first class citizen
    # m = list(map(map_mult_2,l))
    m = list(map(lambda i:i*2,l))
    print(m)
    print(50*'-')
    hello2(firstName="Fred",name="GAURAT")

if __name__ == '__main__':
    main()