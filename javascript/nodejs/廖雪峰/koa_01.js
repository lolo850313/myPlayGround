// 导入koa，和koa 1.x不同，在koa2中，我们导入的是一个class，因此用大写的Koa表示:
const Koa = require('koa');

// 创建一个Koa对象表示web app本身:
const app = new Koa();


// app.use(function)
// 将给定的中间件方法添加到此应用程序。app.use() 返回 this, 因此可以链式表达.
// app.use(someMiddleware)
// app.use(someOtherMiddleware)

// 对于任何请求，app将调用该异步函数处理请求：

// 参数ctx是由koa传入的封装了request和response的变量，
// 我们可以通过它访问request和response，
// next是koa传入的将要处理的下一个异步函数。

app.use(async (ctx, next) => {
    await next();
    ctx.response.type = 'text/html';
    ctx.response.body = '<h1>Hello, koa 01!</h1>';
});

// 在端口3000监听:
app.listen(3000);
console.log('app started at port http://127.0.0.1:3000/...');