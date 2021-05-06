// 在函数外部自然无法读取函数内的局部变量。
function f1() {
    var n = 999
    
}

console.log(n)