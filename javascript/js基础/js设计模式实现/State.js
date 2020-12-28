// 根据情况进行不一样的方案，比如你想去旅游，明确自己有多少钱然后选择旅游方式。
let strategies = {
    "rich" : function () {
        console.log("You can go with plane")
    },
    "poor" : function () {
        console.log("Oh, You can go with your feet")
    },
    "middle" : function () {
        console.log("You can go with train")
    }
}

let howShouldGo = function (money) {
    return strategies[money]()
}

console.log(howShouldGo("rich"))