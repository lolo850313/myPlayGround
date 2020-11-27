import asyncio,threading

@asyncio.coroutine
def hello():
    print("hello world (%s)" % threading.currentThread())
    r = yield from asyncio.sleep(1)
    print("hello again (%s)" % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()