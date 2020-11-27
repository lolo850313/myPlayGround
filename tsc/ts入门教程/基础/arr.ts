//[类型 + 方括号]表示数组
let fibonacci: number[] = [1, 1, 2, 3, 5]

//也可以用数组泛型来表示数组
let fibonacci2: Array<number> = [1, 1, 2, 3, 5]

//使用接口表示数组
interface NumberArray {
    [index: number] : number
}

let fibonacci3 : NumberArray =  [1, 1, 2, 3, 5]

//类数组
// function sum() {
//     let args: number[] = arguments
// }

function sum() {
    let args: {
        [index:number] : number;
        length : number;
        callee: Function
    } = arguments
}

// IAguments 是typescript定义好的类型
// interface IArguments  {
//     [index : number] : number;
//     lenght : number;
//     callee : Function
// }

function sum2() {
    let args : IArguments  = arguments
}
