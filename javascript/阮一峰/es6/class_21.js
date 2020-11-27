//es5
function Point1(x, y) {
    this.x = x
    this.y = y
}

Point1.prototype.toString = function () {
    return '(' + this.x + ', ' + this.y + ')'
}

var p = new Point1(1, 2)

//es6
class Point2{
    constructor(x, y){
        this.x = x
        this.y = y
    }

    // 定义“类”的方法的时候，前面不需要加上function这个关键字
    // 直接把函数定义放进去了就可以了
    toString(){
        return '(' + this.x + ', ' + this.y + ')'
    }
}
// getter与setter
class MyClass {
    constructor(){

    }

    get prop(){
        return 'getter'
    }
    set prop(value){
        console.log('setter: ' + value)
    }
}

let inst = new MyClass()
inst.prop = 123

console.log(inst.prop)

// 存值函数和取值函数是设置在属性的 Descriptor 对象上的。
class CustomHTMLElement{
    constructor(element){
        this.element = element
    }

    get html(){
        return this.element.innerHTML
    }

    set html(value){
        this.element.innerHTML = value
    }
}

var descriptor = Object.getOwnPropertyDescriptor(
    CustomHTMLElement.prototype, "html"
)

console.log('get' in descriptor,'set' in descriptor)

// static关键字，就表示该方法不会被实例继承，
// 而是直接通过类来调用，这就称为“静态方法”。
class Foo{
    static classMethod(){
        return 'hello'
    }
}

Foo.classMethod()

var foo = new Foo()

// foo.classMethod()

// 父类的静态方法，可以被子类继承。
class Bar extends Foo{

}

