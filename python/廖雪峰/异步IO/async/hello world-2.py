import asyncio,threading

async def hello():
    print("hello world (%s)" % threading.currentThread())
    r = await asyncio.sleep(1)
    print(r)
    print("hello again (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()