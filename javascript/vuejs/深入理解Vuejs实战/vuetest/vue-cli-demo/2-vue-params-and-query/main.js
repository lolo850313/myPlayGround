import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from "./pages/Home.vue"
import Detail from './pages/Detail.vue'

Vue.use(VueRouter)

const routes = [
	{path : "/home",component : Home,name : "Home",
		children:[
			{path:"detail", component:Detail, name: "Detail"},
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
