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
        const len = this.followList.length

        if (len > 0) {
            for (const user of this.followList) {
                user.update()
            }
        }
    },

    //添加新用户
    add(user) {
        this.followList.push(user)
    },

    //移除用户
    remove(user) {
        idx = this.followList.indexOf(user)

        if (idx != -1) {
            this.followList.splice(idx, 1)
        }
    },

    //总用户数
    count(){
        return this.followList.length
    },

   
}

 //新建用户的类
 class User {
    constructor(props) {
        super(props);
        
    }
    
}

officialAccount.notify()