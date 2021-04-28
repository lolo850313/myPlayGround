const Koa = require('koa');

const app = new Koa();

// ctx.url相当于ctx.request.url，ctx.type相当于ctx.response.type
app.use(async (ctx, next) => {
    // 打印URL
    console.log(`${ctx.request.method}  ${ctx.request.url}`);
    // 调用下一个middleware
    await next();
});

app.use(async (ctx, next) => {
    const start = new Date().getTime()

    await next()

    const ms = new Date().getTime() - start

    console.log(`Time : ${ms}ms`);

});

app.use(async (ctx, next) => {
    await next();
    ctx.response.type = 'text/html';
    ctx.response.body = '<h1>Hello, koa 02!</h1>';
});

app.listen(3000);
console.log('app started at port http://127.0.0.1:3000/...');