const PUFF_CAKE = "PUFF_CAKE"

const CHEESE_CAKE = "CHEESE_CAKE"

class PuffCake {
    constructor() {
        this.name = "泡芙蛋糕"
    }
}

class CheeseCake {
    constructor() {
        this.name = "奶酪蛋糕"
    }
}
class CakeMaker {
    constructor(type) {
        if (type === PUFF_CAKE) {
            this.cake = new PuffCake()
        }
        else if (type === CHEESE_CAKE) {
            this.cake = new CheeseCake()
        }
        else {
            console.log("invalid cake")
        }
    }
}

stirIngredients() {
    console.log(`开始搅拌${this.cake.name}`)
}

pourIntoMold() {
    console.log(`将${this.cake.name}倒入模具`)
}