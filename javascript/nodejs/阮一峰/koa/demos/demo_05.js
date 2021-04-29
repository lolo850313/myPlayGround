const  Koa = require('koa')
const fs = require('fs')

const app = new Koa()

const main = (ctx) => {
    if (ctx.request.path !== '/') {
        ctx.response.type = 'html'
        ctx.response.body = '<a href="/">Index Page</a>'
    } else {
        ctx.response.body = 'hello world'
    }
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');