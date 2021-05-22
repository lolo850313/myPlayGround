// map,forEach相同点：
// 都支持3个参数，item当前每一项，index当前索引值，arr原数组
// 匿名函数都指向window，
// 只能遍历数组

let arr = ['a', 'b', 'c', 'd', 'e']
arr.forEach(function (item, index, arr) {
    console.log(item);
    console.log(index);
    console.log(arr);
    console.log(this);
}, 123) //123表函数中this的指向，如果不写，则this指向windows

arr.map(function (item, index, arr) {
    console.log(item);
    console.log(index);
    console.log(arr);
    console.log(this);
}, 123)

