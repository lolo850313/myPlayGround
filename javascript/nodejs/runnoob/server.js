var http = require("http")

http.createServer(function (request, response) {
    // text/html的意思是将文件的content-type设置为text/html的形式，
    // 浏览器在获取到这种文件时会自动调用html的解析器对文件进行相应的处理。

    // 2、text/plain的意思是将文件设置为纯文本的形式，
    // 浏览器在获取到这种文件时并不会对其进行处理。
    response.writeHead(200, {'content-type' : 'text/plain'})

    response.end("hello1")
}).listen(8888)

http.createServer(function (request, response) {
    response.writeHead(200, {'content-type' : 'text/plain'})

    response.end("hello2")
}).listen(8889)

console.log("serve is running at http://127.0.0.1:8888");