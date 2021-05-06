// 函数内部可以直接读取全局变量。

var n = 999
function f1() {
    console.log(n)
}

f1()