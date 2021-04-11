<template>
    <div>
        <div>page2</div>
        <div>id:{{$route.query.id}}</div>
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
        console.log(this.$route.query.id);
    },
}
</script>