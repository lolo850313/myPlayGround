//用户
const user = {
    update() {
        console.log("公众号更新了内容")
    }
}

//公众号
const officialAccount = {
    followList : [ user ],
    notify () {

    }
}