import timeit

def init_loop():
    r = []
    for i in range(100):
        r.append(i)

def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]


def main():
    t1 = timeit.timeit('init_loop()', setup="from __main__ import init_loop")
    t2 = timeit.timeit('init_map()', setup="from __main__ import init_map")
    t3 = timeit.timeit('init_comp()', setup="from __main__ import init_comp")

    print("init_loop",f"{t1:.2} s")
    print("init_map",f"{t2:.2} s")
    print("init_comp",f"{t3:.2} s")

if __name__ == '__main__':
    main()