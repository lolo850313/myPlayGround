const http = require("http")

const hostname = '127.0.0.1'

const port = 3000

const server = http.createServer((reqest,response) => {
    response.statusCode = 200
    response.setHeader('content-Type' , "text/plain")
    response.end("hello world\n")
})

server.listen(port, hostname, () => {
    console.log(`服务器运行在 http://${hostname}:${port}/`);
})