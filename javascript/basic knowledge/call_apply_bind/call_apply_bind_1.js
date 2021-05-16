// js中call(),apply(),bind()的用法 https://www.runoob.com/w3cnote/js-call-apply-bind.html
let name = "小王"
let age = 17
let obj = {
    name : "小张",
    objAge : age,
    myFun: function () {
        console.log(this.name + "年龄" + this.age)
    }
}
console.log(obj.objAge)
obj.myFun()

var fav = '盲僧'
function shows() {
    console.log(this)
    console.log(this.fav)
}

shows()

// 第一个this指向obj,第二个指向windows