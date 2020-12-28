// 故名思意，一座工厂源源不断产出一样的产品，流水线作业。没错，工厂模式就是这样。

class Person {
    constructor(name) {
        this.name = name
    }
    
    getName() {
        console.log(this.name)
    }
}

class Factory {
    static create(name) {
        return new Person(name)
    }
}

Factory.create('lolo').getName()