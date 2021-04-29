const  Koa = require('koa')
const fs = require('fs.promised')

const app = new Koa()

const main = async (ctx, next) => {
    ctx.response.type = 'html'
    ctx.response.body = await fs.readFile("./javascript/nodejs/阮一峰/koa/demos/template.html", 'utf-8')
}

app.use(main);

app.listen(3000)

console.log('serve running at http://127.0.0.1:3000/');