// // 2.基本用法
// // Promise对象是一个构造函数，生成Promise实例
// // resolve,reject是由js引擎提供，不需要个人部署。
// // resolve将Promise对象的状态从“pending”变为“fulfilled”
// // reject将Promise对象的状态从“pending”变为“rejected”
// const promise = new Promise(function (resolve, reject) {
//     if () {
//         resolve(value)
//     }else{
//         reject(error)
//     }
// })

// //Promise实例生成后，可以用then分别指定resolved和rejected状态的回调函数
// promise.then(function (params) {
//     //success
// }, function (params) {
//     //failure
// })


function timeout(ms) {
    return new Promise((resolve, reject) => {
        // setTimeout(function, milliseconds, param1, param2, ...)
        // param1, param2, ... 可选。传给执行函数
        setTimeout(resolve, ms, 'done')
    })
}

timeout(1000).then((value) => {
    console.log(value)
})

//promise新建后会立即执行
let promise = new Promise(function (resolve, reject) {
    console.log('Promise')
    resolve() //resolve() 就是后面那个匿名函数 console.log('resolved')
})

promise.then(function () {
    console.log('resolved')
})

console.log('hi')

//实现ajax
const getJSON = function (url) {
    const promise = new Promise(function (resolve, reject) {
        const handler = function () {
            if (this.readyState !== 4) {
                return
            }
            if (this.status === 200) {
                resolve(this.reponse)
            } else {
                reject(new Error(this.statusText))
            }
        }

        const client = new XMLHttpRequest()
        //xhrReq.open(method, url, async, user, password);  
        //async为false，则send()方法知道收到答复前不会返回
        client.open("GET", url) 
        // 当 readyState 的值改变的时候，callback 函数会被调用。
        client.onreadystatechange = handler
        client.responseType = "json"
        // 设置HTTP请求头部的方法。此方法必须在open()方法和send()之间调用。
        client.setRequestHeader("Accept", "application/json")
        client.send()
    })

    return promise
}

getJSON("/post.json").then(
    function (json) {
        console.log('Contents: ' + json)
    },
    function (err) {
        console.log('出错误了', err)
    }
)