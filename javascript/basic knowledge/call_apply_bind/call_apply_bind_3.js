// call,apply,bind区别在于传参

let name = "小王"
let age = 17
let obj = {
    name : "小张",
    objAge : this.age,
    myFun: function (fm, t) {
        console.log(this.name + "年龄" + this.age, " 来自 " + fm + "去往" + t)
    }
}
let db = {
    name : "新 小张",
    age : 99,
}
let fm = "成都", t = "上海"
obj.myFun.call(db, fm, t)
obj.myFun.apply(db,[fm, t])
obj.myFun.bind(db, [fm, t])() 
obj.myFun.bind(db, fm, t)() 