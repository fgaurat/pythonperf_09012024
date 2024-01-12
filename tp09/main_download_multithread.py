import requests
from bs4 import BeautifulSoup
import time
import threading

def download(url_log):
    log_file = url_log.split('/')[-1]
    response = requests.get(url_log)
    with open(log_file,'w') as f:
        f.write(response.text)

def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if ".log" in a['href']]

    all_threads=[]
    
    for url in all_a:
        th = threading.Thread(target=download,args=[url])
        all_threads.append(th)

    [th.start() for th in all_threads]

    [th.join() for th in all_threads]

    end = time.perf_counter()

    print(f"{end-start:.3}s")
    # 0.5 single
    # 0.1 multithread
    # 0.23s threadpool (5)
    # 0.11s threadpool (10)
    # 0.12s async (10)
    # 0.16s async workers (10)




if __name__ == '__main__':
    main()