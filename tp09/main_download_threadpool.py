import requests
from bs4 import BeautifulSoup
import time
from  concurrent.futures import ThreadPoolExecutor


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

    # for url in all_a:
    #     download(url)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(download,all_a)

    end = time.perf_counter()

    print(f"{end-start:.2}s")
    # 0.5 single
    # 0.1 multithread
    # 0.23s threadpool (5)
    # 0.11s threadpool (10)




if __name__ == '__main__':
    main()