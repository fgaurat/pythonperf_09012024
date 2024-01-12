import asyncio

import threading
async def add(a,b):
    print(threading.current_thread().name)
    return a+b

async def main():
    print(threading.current_thread().name)
    # print('Hello ...')
    # await asyncio.sleep(1)
    # print('... World!')
    # a = await add(2,3)
    # b = await add(2,3)
    c = [add(2,3),add(2,3),add(2,3),add(2,3),add(2,3),add(2,3)]
    # print(c)
    r = await asyncio.gather(*c)
    # print(r)

if __name__ == '__main__':
    print(threading.current_thread().name)
    asyncio.run(main())