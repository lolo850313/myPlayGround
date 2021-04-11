<template>
    <div>
        <div>home</div>
        <router-link :to="{name : 'Page1'}" tag="button">goto page1</router-link>
        <router-link :to="{name : 'Page2'}" tag="button">goto Page2</router-link>
        <router-view></router-view>
    </div>
</template>