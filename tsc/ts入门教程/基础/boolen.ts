//布尔值
let  isDone: boolean = false;

//数值
let decLiteral: number = 6

let infNumber: number = Infinity

//字符串
let myName: string = "Tom"
let myAge: number = 30
//模板字符串
let sentence: string = `hello my name is ${myName}. 
i'll be ${myAge + 1} years old next month. `

function alertName():void {
    alert('myName is tom')
}

let unusable: void = undefined

function getLength(something: string | number): number {
    return something.length;
}

function getString(something: string | number): string {
    return something.toString();
}
