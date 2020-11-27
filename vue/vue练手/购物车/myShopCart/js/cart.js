var vm = new Vue({
    el : '#app',
    data:{
        
    },
    // 全局过滤器
    filters:{

    },
    // 开始执行
    mounted:function(){
        this.getAddressList()
    },
    methods:{
        getAddressList:function(){
			var _this = this;
			this.$http.get('./data/address.json',{'id':123}).then(function(res){
				_this.addressList = res.data.result;
			})
		},
    }
})

// 局部过滤器
// vue.filter()

