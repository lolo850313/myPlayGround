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
    
}