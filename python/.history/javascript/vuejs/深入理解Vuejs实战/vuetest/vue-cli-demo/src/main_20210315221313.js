import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import Home from 'pages/Home.vue'
import Page1 from 'pages/Page1.vue'
import Page2 from 'pages/Page2.vue'

Vue.use(VueRouter)

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
