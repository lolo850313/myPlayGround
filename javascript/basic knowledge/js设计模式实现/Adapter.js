// let googleMap = {
//     show : function () {
//         console.log('googleMap show!')
//     }
// }

// let baiduMap = {
//     show : function () {
//         console.log('baiduMap show!')
//     }
// }

// let renderMap = function (map) {
//     if(map.show instanceof Function) {
//         map.show()
//     }
// }

// renderMap(googleMap)
// renderMap(baiduMap)

// 能够运行是因为百度地图和谷歌地图用的同一种show方法，
//但是我们在不知道对方使用的函数接口的时候，
//我们就不能这样用了（可能百度是使用了display方法来显示）

let googleMap = {
    show : function () {
        console.log('googleMap show!')
    }
}

let baiduMap = {
    display : function () {
        console.log('baiduMap show!')
    }
}

let renderMap = function (map) {
    if(map.show instanceof Function) {
        map.show()
    }
}

let baiduMapAdapter = {
    show: function(){
        return baiduMap.display()
    }
}

renderMap(googleMap)
renderMap(baiduMapAdapter)