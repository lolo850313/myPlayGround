// C:\\个人文件夹\\input.txt
var fs = require('fs')

var readStream = fs.createReadStream('C:\\个人文件夹\\input.txt')

var writeStream = fs.createWriteStream('C:\\个人文件夹\\output.txt')

readStream.pipe(writeStream)


console.log("finish")