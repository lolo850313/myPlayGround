import asyncio

async def hello():
    print("hello world")
    r = await asyncio.sleep(1)
    print(r)
    print("hello again")

loop = asyncio.get_event_loop()

loop.run_until_complete(hello())
loop.close()