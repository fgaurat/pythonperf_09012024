import asyncio

async def download(url):
    pass

async def main():
    a = [download(url)]
    result = await a
    print(a)

if __name__ == '__main__':
    asyncio.run(main())