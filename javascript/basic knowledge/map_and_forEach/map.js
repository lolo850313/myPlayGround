// map,forEach相同点：
// 都支持3个参数，item当前每一项，index当前索引值，arr原数组
// 匿名函数都指向window，
// 只能遍历数组

// 不同点：
// map返回一个新数组，新数组中元素为原数组调用函数处理后的值，map不会改变原数组
let arr = [0,2,4,6,8]
let str = arr.map(function (item, index, arr) {
    console.log(this);
    console.log(item);
    console.log(index);
    console.log(arr);
    return item/2
}, this)

console.log(str);

