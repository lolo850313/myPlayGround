const { createRequireFromPath } = require("module");

var fs =  require("fs")
var data = fs.readFileSync("C:\\个人文件夹\\input.txt")

console.log(data.toString())
console.log("end")
