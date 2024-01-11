import requests
from bs4 import BeautifulSoup
import time

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

    for url in all_a:
        download(url)

    end = time.perf_counter()

    print(f"{end-start:.2}s")
    # 0.5




if __name__ == '__main__':
    main()