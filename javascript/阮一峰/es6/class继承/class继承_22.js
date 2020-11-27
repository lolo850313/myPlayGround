class Point {

}
class ColorPoint extends Point{
    constructor(){
        super(x, y)
        this.color = color
    }

    toString() {
        return this.color + " " + super.toString()  // 调用父类的toString()
    }
}

class A {
    constructor(){
        console.log(new.target.name) //new.target指向正在执行的函数
    }
    static hello(){
        console.log("hellow")
    }
}

class B extends A {
    constructor(){
        super() // super代表了父类的构造函数。但返回的是子类B的实例。即
        //super内的this指向B的实例。
        //因此super()相当于A.prototype.constructor.call(this)
    }
}

B.hello() //父类的静态方法，也会被子类继承

console.log(Object.getPrototypeOf(ColorPoint)) //Object.getPrototypeOf方法可以用来从子类上获取父类。
console.log(Object.getPrototypeOf(ColorPoint) === Point)

new A() //A
new B() //B