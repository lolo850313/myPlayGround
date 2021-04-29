const  Koa = require('koa')
const compose = require('koa-compose')
const app = new Koa()

const main = (ctx, next) => {
    ctx.response.body =  'Hello World';
}

const logger = (ctx, next) => {
    console.log(`${Date.now()} ${ctx.request.method} ${ctx.request.url}`);
    next()
}

const middlewares = compose([logger, main])

app.use(middlewares);

app.listen(3000)

console.log('serve running at http://127.0.0.1:3000/');