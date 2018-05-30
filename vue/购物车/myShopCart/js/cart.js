var vm = new Vue({
    el : '#app',
    data:{
        title :'hello vue'
    },
    // 全局过滤器
    filters:{

    },
    // 开始执行
    mounted:function(){
        this.cartview()
    },
    methods:{
        cartview : function(){
            this.title = "hello vueeee"
        }
    }
})

// 局部过滤器
// vue.filter()

