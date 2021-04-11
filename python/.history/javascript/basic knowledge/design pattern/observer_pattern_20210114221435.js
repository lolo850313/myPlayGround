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

    // 公众号更新时候调用的通知函数
    notify () {

    }
}