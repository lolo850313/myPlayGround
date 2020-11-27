// C:\\个人文件夹\\input.txt
var fs = require('fs')

var data = ''

var readerSteam = fs.createReadStream('C:\\个人文件夹\\input.txt')

readerSteam.setEncoding('utf-8')

readerSteam.on('data', function (chunk) {
    data += chunk
    console.log(chunk)
})

readerSteam.on('end', function () {
    console.log(data)
})

readerSteam.on('error', function (err) {
    console.log(err.stack)
})

console.log("finish")