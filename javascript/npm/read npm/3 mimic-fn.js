// 每天阅读一个 npm 模块（3）- mimic-fn https://zhuanlan.zhihu.com/p/43144298

// mimic-fn通过对原函数的复制从而模仿原函数的行为，可以在不修改原函数的前提下，扩充函数的功能

// mimic-fn的使用实例
const mimicFn = require("mimic-fn")

function foo() {}

foo.date = "2018-1"

function wrapper(){
    return foo;
}

console.log(wrapper.name)

mimicFn(wrapper,foo)

console.log(wrapper.name)

console.log(wrapper.date)

// mimic源码
module.exports = (to, from) =>{
    for(const prop of Object.getOwnPropertyNames(from).concat(Object.getOwnPropertySymbols(from))){
        Object.defineProperty(to, prop, Object.getOwnPropertyDescriptor(from, prop))
    }

    return to
}
