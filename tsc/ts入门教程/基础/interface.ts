interface Person {
    name : string;
    age : number;
}

let tom1 : Person = {
    name: "Tom",
    age: 22
}

//接口可选属性
interface Person2 {
    name: string;
    age?: number;
}

let tom2 : Person2 = {
    name: "Tom2",
}

//任意属性
interface Person3 {
    name : string;
    age?: number;
    [propName: string]: any;
}

let tom3 : Person3 = {
    name: "Tom",
    age:25,
    gender:"1"
}

//只读属性
interface Person4 {
    readonly id: number;
    name: string;
    age?: number;
    [propName: string]: any;
}

let tom4: Person4 = {
    id : 123213,
    name:"Tom",
    gender: "a"
}

tom4.id = 123