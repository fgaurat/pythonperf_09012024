import celery_tasks
from celery import Celery,signature,group,chain
from bs4 import BeautifulSoup
import httpx


def main():
    app = Celery('hello', broker='amqp://guest@localhost//',backend="redis://localhost:6379/0")
    url = "https://logs.eolem.com/"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_a = [url+a['href'] for a in soup.find_all('a') if ".log" in a['href']]

    download_task = signature('celery_tasks.download')
    download = download_task.delay(all_a[0])
    print(download.get())
    
    # # All downloads
    # download_tasks = [signature('celery_tasks.download',args=[url]) for url in all_a]
    # download_group = group(download_tasks)
    # result = download_group()
    # all_content = result.get()
    
    # # All save
    # save_tasks = [signature('celery_tasks.save',args=[to_save]) for to_save in all_content]
    # save_group = group(save_tasks)
    # save_group()

    for url in all_a:
        chain(signature('celery_tasks.download',args=[url]),signature('celery_tasks.save'))()
        
        # chain_task = chain(signature('celery_tasks.download',args=[url]),signature('celery_tasks.save'))
        # chain_task()
        # res = chain_task()
        # res.get()



def main_hello_remote():
    app = Celery('hello', broker='amqp://guest@localhost//',backend="redis://localhost:6379/0")
    
    hello_task = app.send_task('celery_tasks.hello')
    hello = hello_task.get()
    print(hello)
    
    tasks = list(app.tasks.keys())
    print(tasks)
    
    hello_task = signature('celery_tasks.hello')
    hello = hello_task.delay("fred")
    print(hello.get())

    # i = app.control.inspect()
    # # Show the items that have an ETA or are scheduled for later processing
    
    # print(i.reserved())
    # print(i.scheduled())

    # print(i.active())

    # print(i.reserved())



def main_local():
    hello_task = celery_tasks.hello.delay()


    hello = hello_task.get()
    print(hello)

if __name__ == '__main__':
    main()