Page({
    data: { name: '' },
    buttonHandler(event) 
    {
        wx.navigateTo({
            url : '../second/second'
        })
    }
});