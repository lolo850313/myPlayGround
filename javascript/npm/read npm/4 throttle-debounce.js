
// 每天阅读一个 npm 模块（4）- throttle-debounce https://zhuanlan.zhihu.com/p/43410181

// throttle 是节流 debounce是防抖动，避免短时间内函数多次执行

// 简单用法
import {throttle, debounce} from "throttle-debounce"

function foo() {console.log('foo...')}
function bar() {console.log('bar...')}

const fooWrapper = throttle(200, foo)

for (let i=1; i<10; i++){
    setTimeout(fooWrapper, i*30)
}

const barWrapper = debounce(200, bar)
for (let i = 0; i < 10; i++) {
    setTimeout(barWrapper, i*30)    
}

// 源码学习
function throttle(delay, callback) {
    let timeoutID = 0
    let lastExec =  0

    function wrapper() {
        const self = this
        
    }
}