<template>
    <div>
        <div>Detail</div>
        <div>{{$route.query.id ? '修改' : '新建'}}</div>
        <div>name: <input v-model="detail.name"></div>
        <div>text: <input v-model="detail.text"></div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            detail : {
                name:"",
                text : ""
            }
        }
    },
    watch:{
        $route(from, to){
            console.log({to, from});

            if(to.query.id !== from.query.id){
                this.updateDetail()
            }
        }
    },

    methods: {
        updateDetail(){
            const id = this.$route.query.id

            if (id) {
                this.detail = {
                    name : `name-${id}`,
                    text : `text-${id}`,
                }
            } else {
                this.detail = {
                    name : "",
                    text : "",
                }
            }
        }
    },
    mounted() {
        console.log(this.$route.params);
    },
}
</script>