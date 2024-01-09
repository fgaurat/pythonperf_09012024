from collections import deque

def main():
    l = [10,20,30]
    print(l)
    l.append(40)
    print(l)
    last_value = l.pop()
    print(last_value)
    print(l)
    l.insert(0,0)
    print(l)
    first_value = l.pop(0)
    print(first_value)
    print(l)
    
    print(50*'-')
    
    l = [10,20,30]
    d = deque(l)
    print(d)
    d.appendleft(0)
    print(d)
    f = d.popleft()
    print(d)
    print(f)
    t = max( 4,5,6,7)
    print(t)
    t = max( [4,5,6,7])
    print(t)



if __name__ == '__main__':
    main()