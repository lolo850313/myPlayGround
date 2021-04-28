const nunjuncks = require('nunjucks')

function createEnv(path, opts) {
    var autoescape = opts.autoescape === undefined ? true : opts.autoescape,
        noCache = opts.noCache || false,
        watch = opts.watch || false,
        throwOnUndefined  = opts.throwOnUndefined   || false,
        env = new nunjuncks.Environment(
            new nunjuncks.FileSystemLoader('views', {
                noCache : noCache,
                watch : watch,
            }),
            {
                autoescape : autoescape,
                throwOnUndefined : throwOnUndefined
            }
        )
    
    if (opts.filters) {
        for (const f in opts.filters) {
            env.addFilter(f, opts.filters[f])
        }
    }

    return env
};

var env = createEnv(__dirname + 'views', {
    watch : true,
    filters : {
        hex : function (n) {
            console.log(n);
            return '0x' + n.toString(16)
        }
    }
});

var s = env.render('hello.html', { name : '小明'});

console.log(s);