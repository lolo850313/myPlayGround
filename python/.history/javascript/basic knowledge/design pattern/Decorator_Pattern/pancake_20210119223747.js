class Pancake {
    constructor() {
        this.name = '煎饼果子'
    }

    getName() {
        return this.name()
    }

    getPrice() {
        return 5
    }
    
}

// 装饰器
class PancakeDecorator {
    constructor(pancake) {
        this.Pancake = pancake
    }
    
    getName (){
        return `${this.pancake.getName()}`
    }

    getPrice (){
        return this.pancake.getPrice()
    }
}

//加鸡蛋
class PancakeDecoratorWithEgg extends PancakeDecorator {
    getName() {
        return `${this.pancake.getName()} ➕鸡蛋`
    }

    getPrice() {
        return this.pancake.getPrice() + 2
    }
}

//加香肠
class PancakeDecoratorWithSausage extends PancakeDecorator {
    getName() {
        return `${this.pancake.getName()} ➕香肠`
    }

    getPrice() {
        return this.pancake.getPrice() + 1.5
    }
}