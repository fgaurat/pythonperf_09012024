import asyncio

async def ma_coroutine():
    # start = time.time()
    # while time.time() - start < 3:
    #     pass
    print("ma_coroutine")
    await asyncio.sleep(1)
    print("après sleep")


def ma_callback(task):
    if task.cancelled():
        print('cancelled')
    else:
        print('pas cancelled')


async def main():
    # await ma_coroutine()
    task = asyncio.create_task(ma_coroutine())
    task.add_done_callback(lambda t: ma_callback(t))
    # task.add_done_callback(ma_callback)

    await task
    print("end")

if __name__ == "__main__":
    asyncio.run(main())




