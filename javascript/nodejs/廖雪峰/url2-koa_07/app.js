const Koa = require('koa');
const bodyParser = require('koa-bodyparser');
const fs = require('fs');
const router = require('koa-router')()

const app = new Koa();

console.log(__dirname+ '/controllers');
var files = fs.readdirSync(__dirname + '/controllers')

var js_files = files.filter((f) => {
    return f.endsWith(".js")
})

app.use(async (ctx, next) => {
    console.log(`Process ${ctx.request.method} ${ctx.request.url}`);
    await next()
});

app.use(bodyParser());

for (const f of js_files) {
    console.log(`process controller: ${f}...`);

    // 遍历读取controllers内所有文件，将文件内exports的对象赋值为mapping
    let mapping = require(__dirname + '/controllers/' + f)

    for (const url in mapping) {
        if (url.startsWith("GET")) {
            // 如果url类似“GET XXX”
            var path = url.substring(4)

            // 得到exports内url对应的async函数
            var fn = mapping[url]

            router.get(path, fn)

            console.log(`register URL mapping: GET  ${path}`);
        
        } else if (url.startsWith("POST")) {
            var path = url.substring(5)

            // 得到exports内url对应的async函数
            var fn = mapping[url]

            router.post(path, fn)

            console.log(`register URL mapping: POST ${path}`);
        } else {
            console.log(`invalid URL: ${url}`);
        }
    }
}


app.use(router.routes())

app.listen(3000);
console.log('app started at port http://127.0.0.1:3000/...');