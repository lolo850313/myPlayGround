// const app=getApp()
Page({
    data:{
        items : [],
    },
    onLoad(){
        const that = this
        wx.request({
            url:'http://localhost:3000/items', 
            success(res) {
                // res是服务器发送过来的json数据
                console.log(res)
                that.setData({
                    items : res.data
                })
            }
        })
    }
})