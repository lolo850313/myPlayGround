// 单例模式就是保证一个类仅有一个实例，并提供一个访问它的全局访问点。
// 其实这有一点像我们vuex当中的实现，也是一个全局的状态管理，并且提供一个接口访问。

//结果是false，跟预期不一样
let Singleton = function (name) {
    this.name = name
}

Singleton.prototype.getName = function () {
    console.log(this.name)
}

Singleton.getInstance = function () {
    let instance = null
    return function (name) {
        if(!instance){
            instance = new Singleton(name)
        }
        return instance
    }
}

let a = Singleton.getInstance('alan1')
let b = Singleton.getInstance('alan1')

console.log(a)
console.log(b)