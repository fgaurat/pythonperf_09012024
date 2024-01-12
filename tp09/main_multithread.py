import threading

lock = threading.Lock()

def tl01():
    with lock:
        print(threading.current_thread().name)
        for i in range(10):
            print('tl01',i)

def tl02():
    with lock:
        print(threading.current_thread().name)
        for i in range(10):
            print('tl02',i)

def main():
    th1 = threading.Thread(target=tl01)
    th2 = threading.Thread(target=tl02)

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(threading.current_thread().name)
    print('fin')

if __name__ == '__main__':
    main()