import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from "./pages/Home.vue"
import Page1 from 'pages/Page1.vue'
import Page2 from 'pages/Page2.vue'

Vue.use(VueRouter)

const routes = [
	{
		path : "/home",
		component : Home,
		name : "Home",
		children:[
			{path:"page1", component:Page1, name: "Page1"},
			{path:"page2", component:Page2, name: "Page2"},
		]
	},
	{path:"*", redirect: {name:"Home"}}
]

const router = new VueRouter({
	routes
})

new Vue({
	el:"#app",
	router,
	render: h => h(App),
})
