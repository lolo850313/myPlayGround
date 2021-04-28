const Koa = require('koa');

// 注意require('koa-router')返回的是函数
// 导入koa-router的语句最后的()是函数调用
const router = require('koa-router')()

const app = new Koa();

app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}`);
    await next()
});

// add url-route:
router.get('/hello/:name', async(ctx, next) => {
    var name = ctx.params.name
    ctx.response.body = `<h1>Hello, ${name}!</h1>`
})

router.get('/', async(ctx, next) => {
    ctx.response.body = `<h1>index</h1>`
})

app.use(router.routes())

app.listen(3000);
console.log('app started at port http://127.0.0.1:3000/...');