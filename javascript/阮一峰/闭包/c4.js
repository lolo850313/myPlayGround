// 从外部读取局部变量
// 使用return
function f1() {
    var n = 999
    function f2() {
        console.log(n);
    }
    return f2
}
var res = f1()
res()