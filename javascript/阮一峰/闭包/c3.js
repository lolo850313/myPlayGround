// 一定要使用var命令。
// 如果不用的话，你实际上声明了一个全局变量
function f1() {
    n = 999
    
}
f1()
console.log(n)