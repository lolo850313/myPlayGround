function sum(x , y)  {
    return x + y
}

let mySum = function(x : number, y : number) : number{
    return x + y
}

//手动给mySum添加类型
// 在 TypeScript 的类型定义中，=> 用来表示函数的定义，
// 左边是输入类型，需要用括号括起来，右边是输出类型。
let mySum2 : (x: number, y:number) => number = function(x : number, y : number) : number{
    return x + y
}

//接口方式定义函数
interface SearchFunc {
    (source : string , subString : string) : boolean
}

let mySearch2 : SearchFunc
mySearch2 = function(source : string , subString : string) {
    return source.search(subString) !== -1
}

//可选参数
function buildName(firstName: string, lastName?: string) {
    if (lastName) {
        return firstName + lastName
    } else {
        return firstName
    }    
}

let tomcat = buildName("tom", "cat")

let tom = buildName("ton")

//剩余参数
<<<<<<< HEAD
function push(array : any[], ...items : any[]) {
=======
function push(array : any
    [], ...items : any[]) {
>>>>>>> daef8dd5567c6a2c56d879155dce9433def227cd
    items.forEach(function(item){
        array.push(item)
    })
}

let arr :any[] = []

push(arr, 1, 2, 3)