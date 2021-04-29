const  Koa = require('koa')
const route = require('koa-route');
const app = new Koa()

const main = (ctx) => {
    ctx.response.body = 'hello world'
}

const redirect = (ctx) => {
    ctx.response.redirect('/')
}

app.use(route.get("/", main))
app.use(route.get("/redirect", redirect))


app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');