// class PanCakeMaterials {
//     constructor(vegetableMarketName) {
//         this.vegetableMarketName = vegetableMarketName
//     }

//     getEgg() {
//         if (this.vegetableMarketName == 'VEGETABLE_MARKET_NAME_A') {
//             return 'a-market-egg'
//         }
//         if (this.vegetableMarketName == 'VEGETABLE_MARKET_NAME_B') {
//             return 'b-market-egg'
//         }
//     }
    
// }
// const panCakeMaterials = new PanCakeMaterials("VEGETABLE_MARKET_NAME_A");
// console.log(panCakeMaterials.getEgg());  // a_market_egg

class VegetableMarketProvider {
    provideEgg(){}
}

class FirstVegetableMarketProvider extends VegetableMarketProvider {
    provideEgg() {
        return 'a-market-egg'
    }
}

class SecondeVegetableMarketProvider extends VegetableMarketProvider {
    provideEgg() {
        return 'b-market-egg'
    }
}

class ThirdVegetableMarketProvider extends VegetableMarketProvider {
    provideEgg() {
        return 'c-market-egg'
    }
}

class PanCakeMaterials {
    constructor(vegetableMarketProvider) {
        this.vegetableMarketProvider = vegetableMarketProvider
    }

    getEgg() {
        return this.vegetableMarketProvider.provideEgg()
    }
    
}

const firstVegetableMarketProvider = new FirstVegetableMarketProvider()
const secondVegetableMarketProvider = new SecondeVegetableMarketProvider()
const thirdVegetableMarketProvider = new ThirdVegetableMarketProvider()

const panCakeMaterials = new PanCakeMaterials(firstVegetableMarketProvider);
console.log(panCakeMaterials.getEgg());  // a_market_egg

const secondPanCakeMaterials = new PanCakeMaterials(secondVegetableMarketProvider);
console.log(secondPanCakeMaterials.getEgg());  

const thirdPanCakeMaterials = new PanCakeMaterials(thirdVegetableMarketProvider);
console.log(thirdPanCakeMaterials.getEgg()); 