//公众号
const officialAccount = {
    //关注当前公众号的用户列表
    followList : [],

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

 //用户的类
class User {
    constructor(name) {
        this.name = name
    }

    update() {
        console.log(`${this.name}接受到了公众号的内容更新`)
    }
}

const zhansan = new User("张三")
const lisi = new User("李四")


officialAccount.add(zhansan)
officialAccount.add(lisi)

officialAccount.notify()
console.log(`当前公众号的用户数量是${officialAccount.count()}`)

officialAccount.remove(zhansan)

officialAccount.notify()
console.log(`当前公众号的用户数量是${officialAccount.count()}`)

