function f1() {
    var n = 999
    nAdd = function () {
        n += 1
    }

    function f2() {
        console.log(n);
    }

    return f2
}

var res = f1()

res()

nAdd()

res()