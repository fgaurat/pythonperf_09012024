import asyncio
import requests
import httpx
from bs4 import BeautifulSoup
import time

async def download_httpx(url_log):
    async with httpx.AsyncClient() as client:
        response = await client.get(url_log)

    log_file = url_log.split('/')[-1]
    with open(log_file,'w') as f:
        f.write(response.text)

async def download_requests(url_log):
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, requests.get, url_log)

    log_file = url_log.split('/')[-1]
    with open(log_file,'w') as f:
        f.write(response.text)

async def main():
    start = time.perf_counter()
    url="https://logs.eolem.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if ".log" in a['href']]

    # tasks = [download_requests(url) for url in all_a]
    # await asyncio.gather(*tasks)

    tasks = [download_httpx(url) for url in all_a]
    await asyncio.gather(*tasks)
        

    end = time.perf_counter()

    print(f"{end-start:.2}s")
    # 0.5 single
    # 0.1 multithread
    # 0.23s threadpool (5)
    # 0.11s threadpool (10)
    # 0.12s async (10)




if __name__ == '__main__':
    asyncio.run(main())