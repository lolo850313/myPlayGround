// C:\\个人文件夹\\input.txt
var fs = require('fs')
var zlib = require('zlib')

fs.createReadStream('C:\\个人文件夹\\input.txt')
    .pipe(zlib.createGzip())
    .pipe(fs.createWriteStream('C:\\个人文件夹\\input.txt.gz'))

console.log("finish")