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
        } else {
            this.cake = new CheeseCake()
        }
    }
}