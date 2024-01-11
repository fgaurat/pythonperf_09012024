import os
import time
from multiprocessing import Pool

def f(x):
    t=1
    start = time.time()
    while time.time()-start<1:
        pass
    return x*x

def main():
    print(os.cpu_count())
    with Pool(3) as p:
        r = p.map(f, range(100))
        print(r)    

if __name__ == '__main__':
    main()