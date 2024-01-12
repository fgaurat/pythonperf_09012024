from bs4 import BeautifulSoup
import httpx
import time
import asyncio


async def download(download_queue:asyncio.Queue, save_queue:asyncio.Queue):
    while True:
        url_log = await download_queue.get()
        async with httpx.AsyncClient() as client:
            response = await client.get(url_log)
            d = {
                "url": url_log,
                "content": response.text
            }
            save_queue.put_nowait(d)
        download_queue.task_done()


async def save(save_queue):
    while True:
        d = await save_queue.get()
        url_log = d['url']
        content =d['content']
        log_file = url_log.split('/')[-1]
        with open(log_file, 'w') as f:
            f.write(content)
        save_queue.task_done()


async def main():
    start = time.perf_counter()

    download_queue = asyncio.Queue()
    save_queue = asyncio.Queue()
    nb_workers_download = 10
    nb_workers_save = 3

    url = "https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if ".log" in a['href']]

    tasks = []

    for i in range(nb_workers_download):
        task = asyncio.create_task(download(download_queue, save_queue))
        tasks.append(task)

    for i in range(nb_workers_save):
        task = asyncio.create_task(save(save_queue))
        tasks.append(task)

    for url in all_a:
        download_queue.put_nowait(url)


    await download_queue.join()
    await save_queue.join()

    for task in tasks:
        task.cancel()

    end = time.perf_counter()

    print(f"{end-start:.2}s")
    # 0.5 single
    # 0.1 multithread
    # 0.23s threadpool (5)
    # 0.11s threadpool (10)
    # 0.12s async (10)
    # 0.16s async workers (10)


if __name__ == '__main__':
    asyncio.run(main())
