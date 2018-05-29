// // 阻塞代码
// var fs = require('fs')
// var data = fs.readFileSync('\\lolo\\nodejs\\nodejs of runoob\\2\\input.txt')
// console.log(data.toString())
// console.log('program end!')

// 非阻塞代码
var fs = require('fs')

fs.readFile('\\lolo\\nodejs\\nodejs of runoob\\3 event loop\\input.txt', function (err, data) {
    if(err) {
        console.log(err)
        return
    }
    console.log(data.toString())
})
console.log('program end!')