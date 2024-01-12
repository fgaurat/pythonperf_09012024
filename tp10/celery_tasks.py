from celery import Celery
import httpx

app = Celery('hello', broker='amqp://guest@localhost//',backend="redis://localhost:6379/0")
# pip install "celery[librabbitmq,redis]"

@app.task
def hello(name=""):
    print('hello world from task',name)
    return f'hello world {name}'

@app.task
def download(url):
    response = httpx.get(url)
    d = {
        "url":url,
        "content":response.text
    }
    return d

@app.task
def save(d):
    log_file = d['url'].split("/")[-1]
    content = d['content']
    with open(log_file,'w') as f:
        f.write(content)



