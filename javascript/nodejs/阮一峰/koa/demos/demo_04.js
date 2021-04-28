const  Koa = require('koa')
const fs = require('fs')

const app = new Koa()

const main = (ctx) => {
    ctx.response.type = 'html'
    ctx.response.body = fs.createReadStream('./demo_04.js')
}

app.use(main)

app.listen(3000)
console.log('serve running at http://127.0.0.1:3000/');