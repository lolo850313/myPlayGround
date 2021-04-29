// 不同async/await
function takeLongTime() {
    return new Promise( resolve => {
        setTimeout( () => resolve("long_time_value"), 1000)
    })
}

takeLongTime().then( v => {
    console.log("got", v);
})

// 使用async/await

// akeLongTime() 没有申明为 async。
// 实际上，takeLongTime() 本身就是返回的 Promise 对象，加不加 async 结果都一样，
function takeLongTime() {
    return new Promise( resolve => {
        setTimeout( () => resolve("long_time_value"), 1000)
    })
}

async function test() {
    const v = await takeLongTime()
    console.log("got", v);
}

test()

