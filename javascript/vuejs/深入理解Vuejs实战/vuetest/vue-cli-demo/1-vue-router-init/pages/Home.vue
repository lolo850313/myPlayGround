<template>
    <div>
        <div>home</div>
        <div>
            <input v-model="id">
            <br />
            <!-- 指定<router-link>渲染成某种标签，默认为a -->
            <router-link :to="{name : 'Page1', params:{ id : id }}" tag="button">goto page1</router-link>
            <router-link :to="{name : 'Page2', query :{ id : id }}" tag="button">goto Page 2</router-link>
        
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