// Mixin指的是多个对象合成一个新的对象
const a = {
    a : 'a'
}
const b = {
    b : 'b'
}

const c = {...a, ...b}
console.log(c)