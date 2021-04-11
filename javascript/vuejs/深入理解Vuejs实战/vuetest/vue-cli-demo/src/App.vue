<template>
	<section class="todoapp">
		<header>
			<h1>Todos</h1>
			<input 
			class="new-todo"
			placeholder="请输入你的待办" 
			v-model="newTodo" 
			v-autofocus
			v-on:keyup.enter="addTodo"/>
		</header>
		<section class="main" v-show="todos.length">
		<div>
			<ul class="todo-list">
				<li v-for="todo in todos" 
					v-bind:key="todo.id" 
					v-bind:class="{}"
					>
					<div class="view">
						<input 
							type="checkbox" 
							class="toggle"
							v-model="todo.completed">
						<label v-on:dblclick="editTodo(todo)">{{todo.title}}</label>
						<button class="destroy" v-on:click="removeTodo(todo)"></button>
					</div>
					<input type="text" 
						class="edit"
						v-model="editedTodo.title"
						v-on:keyup.enter="doneEdit(editedTodo)" 
						v-on:keyup.esc="cancleEdit()"
						>
				</li>
			</ul>
		</div>

		<div class="footer">
			<span class="todo-count">
			<strong>{{ remaining }}</strong> {{ remaining | pluralize }} left
			</span>
			<button 
			class="clear-completed"
			v-on:click="removeCompleted">
			clear completed
			</button>
		</div>
		</section>
	</section>
</template>
<script>
// (1) 实现新增备忘。
// (2) 实现备忘列表管理，包括编辑、删除等功能。
// (3) 实现计算与快速移除已完成备忘数。

let id = 1;
export default {
	name : "app",
	data(){
		return {
		todos:[],
		newTodo:"",
		editedTodo :  {}
	}
	},
	computed:{
		remaining(){
		// 注意箭头函数带{}需要{}内有return
			return this.todos.filter( (t) => { return !t.completed} ).length
		// return this.todos.filter(x => !x.completed).length;
		}
	},
	filters : {
		// 处理todo-count中的item单复数形式
		pluralize(num){
			if (num > 1) {
			return "items"
			}
			return "item"
		}
	},
	methods: {
		addTodo() {
			if (!this.newTodo) {
			return
			} 
			this.todos.unshift({
				id:id++,
				title : this.newTodo,
				completed: false
			})
			console.log(this.todos)
			this.newTodo = ""
		},
		editTodo(todo){
			this.editedTodo = {...todo}
		},
		doneEdit(todo){
			this.todos = this.todos.map(x=>{
			// 将todo的值更新为x
			return todo.id === x.id ? {...todo} : {...x}
			})
			this.editTodo = {}
		},
		removeTodo(todo){
			const index = this.todos.findIndex( (x) => {x.id === todo.id})
			this.todos.splice(index, 1)
		},
		removeCompleted(){

			this.todos = this.todos.filter( (t) => { return !t.completed} )
		},
		cancleEdit(){
			this.editedTodo = {}
		}
	},
	directives : {
		autofocus : {
			inserted : function(el){
				el.focus()
			}
		}
	}
}
</script>
<style>
	@import "https://unpkg.com/todomvc-app-css@2.1.0/index.css";
</style>