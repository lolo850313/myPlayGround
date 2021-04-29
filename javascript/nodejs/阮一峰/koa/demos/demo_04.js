const  Koa = require('koa')
const fs = require('fs')

const app = new Koa()

const main = (ctx) => {
    ctx.response.type = 'html'
    ctx.response.body = fs.createReadStream('./javascript/nodejs/阮一峰/koa/demos/template.html')
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');