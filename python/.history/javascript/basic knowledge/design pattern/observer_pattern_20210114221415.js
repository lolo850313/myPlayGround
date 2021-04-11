//用户
const user = {
    update() {
        console.log("公众号更新了内容")
    }
}

//公众号
const officialAccount = {
    //关注当前公众号的用户列表
    followList : [ user ],
    notify () {

    }
}