<template>
    <div>
        <div>home</div>
        <div>
            <input v-model="id">
            <br />
            <!-- 指定<router-link>渲染成某种标签，默认为a -->
            <router-link :to="{name : 'Detail'}" tag="button">新建</router-link>
            <router-link :to="{name : 'Detail', query :{ id : id }}" tag="button">修改</router-link>
        
        </div>
        <router-view></router-view>
    </div>
</template>
<script>
export default {
    data() {
        return {
             id: ""
        }
    },
    //两种data形式都可以
//    data:() =>{
//     return {
//       id: ""
//     }
//   },
    methods: {
        
    },
}
</script>