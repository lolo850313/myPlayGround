// C:\\个人文件夹\\input.txt
var fs = require('fs')
var zlib = require('zlib')

fs.createReadStream('C:\\个人文件夹\\input.txt.gz')
    .pipe(zlib.createGunzip())
    .pipe(fs.createWriteStream('C:\\个人文件夹\\inputDeCompress.txt'))

console.log("finish")