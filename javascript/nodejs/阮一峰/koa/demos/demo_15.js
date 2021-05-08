const  Koa = require('koa')
const app = new Koa()

const main = (ctx) => {
    ctx.throw(404)
    ctx.response.body = 'Page not found'
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');