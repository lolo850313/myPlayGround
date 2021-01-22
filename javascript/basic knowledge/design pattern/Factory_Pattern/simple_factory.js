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

function cakeCategoryMaker(type) {
    let cake
    if (type === PUFF_CAKE) {
        cake = new PuffCake()
    }
    else if (type === CHEESE_CAKE) {
        cake = new CheeseCake()
    }
    else {
        cake = false
    }
    return cake
}
class CakeMaker {
    constructor(type) {
        this.cake = cakeCategoryMaker(type)
    }

    stirIngredients() {
        console.log(`开始搅拌${this.cake.name}`)
    }
    
    pourIntoMold() {
        console.log(`将${this.cake.name}倒入模具`)
    }

    bakeCake() {
        console.log(`开始烘焙${this.cake.name}蛋糕`)
    }
}

const cakeMaker = new CakeMaker(PUFF_CAKE)
cakeMaker.stirIngredients()
cakeMaker.pourIntoMold()
cakeMaker.bakeCake()
