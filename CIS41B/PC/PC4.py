
# async
import asyncio
import random

async def marge(cookiejar, n):
    for x in range(n):
        print('marge producing {}/{}'.format(x+1, n))
        await asyncio.sleep(random.random())
        cookie = str(x+1)
        await cookiejar.put(cookie)

async def homer(cookiejar):
    while True:
        cookie = await cookiejar.get()
        print('homer consuming {}...'.format(cookie))
        await asyncio.sleep(random.random())
        cookiejar.task_done()

async def run(n):
    cookiejar = asyncio.Queue()
    consumer = asyncio.ensure_future(homer(cookiejar))
    await marge(cookiejar, n)
    await cookiejar.join()

loop = asyncio.get_event_loop()
loop.run_until_complete(run(10))
loop.close()
