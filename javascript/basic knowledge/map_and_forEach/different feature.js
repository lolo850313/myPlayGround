// map forEach的区别在于返回值

let arr = ['a', 'b', 'c', 'd', 'e']
let a = arr.forEach(function () {
    return 123
})

let b = arr.map(function () {
    return 123
})

console.log(a); //undefined
console.log(b); // [123,123,123,123,123]

