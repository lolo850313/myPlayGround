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

class PancakeDecorator {
    constructor(pancake) {
        this.Pancake = pancake
    }
    
    getName {
        return `${this.pancake.getName()}`
    }

    getPrice {
        return this.pancake.getPrice()
    }
}