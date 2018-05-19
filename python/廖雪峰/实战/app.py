import logging;logging.basicConfig(level=logging.INFO)


import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    #增加content_type后网页可正常显示，去掉b后浏览器不会自动下载。因为b"<h1>Awesome</h1>"表明他是一个二进制文件。
    return web.Response(body="<h1>Awesome</h1>",content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

