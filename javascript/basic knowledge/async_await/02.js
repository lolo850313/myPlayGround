// await 等待的是一个表达式，这个表达式的计算结果是 Promise 对象
// 或者其它值（换句话说，就是没有特殊限定）。

// 如果它等到的是一个 Promise 对象，await 就忙起来了，
// 它会！！阻塞！！
// 后面的代码，等着 Promise 对象 resolve，然后得到 resolve 的值，作为 await 表达式的运算结果。


// await 后面实际是可以接普通函数调用
function getSomething() {
    return "something"
}

//await 在等 async 函数
async function testAsync(params) {
    return Promise.resolve("hello async")
}

async function test() {
    const v1 = await getSomething()
    const v2 = await testAsync()
    console.log(v1, v2);
}

test()

