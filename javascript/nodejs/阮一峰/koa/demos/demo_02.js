const  Koa = require('koa')
const app = new Koa()

// ctx.response代表 HTTP Response。同样地，ctx.request代表 HTTP Request。
const main = (ctx) => {
    ctx.response.body = 'hello world1'
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');