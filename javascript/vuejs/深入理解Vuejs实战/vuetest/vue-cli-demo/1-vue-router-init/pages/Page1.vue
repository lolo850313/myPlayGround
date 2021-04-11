<template>
    <div>
        <div>page1</div>
        <div>id : {{$route.params.id}}</div>
        
    </div>
</template>
<script>
export default {
    data() {
        return {
            
        }
    },
    methods: {
        
    },
    mounted() {
        console.log(this.$route.params);
    },
}
</script>