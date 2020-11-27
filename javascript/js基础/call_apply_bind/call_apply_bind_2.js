// call,apply,bind都是用来重定义this这个对象的

let name = "小王"
let age = 17
let obj = {
    name : "小张",
    objAge : this.age,
    myFun: function () {
        console.log(this.name + "年龄" + this.age)
    }
}
let db = {
    name : "新 小张",
    age : 99,
}

obj.myFun.call(db)
obj.myFun.apply(db)
obj.myFun.bind(db)() //bind返回的是一个函数，必须调用它才能执行