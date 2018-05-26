// // 阻塞代码
// var fs = require('fs')
// var data = fs.readFileSync('\\lolo\\nodejs\\nodejs of runoob\\2\\input.txt')
// console.log(data.toString())
// console.log('program end!')

// 非阻塞代码
var fs = require('fs')

fs.readFile('\\lolo\\nodejs\\nodejs of runoob\\callback\\2\\input.txt', function (err, data) {
    if(err) return console.error(err)
    console.log(data.toString())
})
console.log('program end!')