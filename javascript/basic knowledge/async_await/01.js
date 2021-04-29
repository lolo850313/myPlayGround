// async 起什么作用:输出的是一个 Promise 对象
async function testAsync() {
    return "hello async"
}

const result = testAsync()

console.log(result);

// async 函数返回的是一个 Promise 对象，所以在最外层不能用 await 获取其返回值的情况下，
// 我们当然应该用原来的方式：then() 链来处理这个 Promise 对象，
testAsync().then( v => {
    console.log(v);
})