const  Koa = require('koa')
const app = new Koa()

// ctx.response代表 HTTP Response。同样地，ctx.request代表 HTTP Request。
const main = (ctx) => {
    if (ctx.request.accepts('xml')) {
        ctx.response.type = 'xml'
        ctx.response.body = '<data>Hello World xml</data>'
    } else if (ctx.request.accepts('json')) {
        ctx.response.type = 'json'
        ctx.response.body = { data: 'Hello World json' }
    } else if (ctx.request.accepts('html')) {
        ctx.response.type = 'html'
        ctx.response.body = '<p>Hello World html</p>';
    } else {
        ctx.response.type = 'test'
        ctx.response.body = 'Hello World text';
    }
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');