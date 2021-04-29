const  Koa = require('koa')
const route = require('koa-route');
const app = new Koa()

const main = (ctx) => {
    ctx.response.body = 'hello world 7'
}

const about = (ctx) => {
    ctx.response.type = 'html'
    ctx.response.body = '<a href="/">Index Page</a>'
}

const logger = (ctx,next) => {
    console.log(`${Date.now()} ${ctx.request.method} ${ctx.request.url}`);
    next()
}

app.use(logger);
app.use(route.get("/", main))
app.use(route.get("/about", about))



app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');