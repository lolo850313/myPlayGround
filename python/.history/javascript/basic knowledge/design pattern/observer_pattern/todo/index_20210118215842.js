// Subject
class Subject {
	constructor() {
		this.observerCollection = [];
	}
	// 添加观察者
	registerObserver(observer) {
		this.observerCollection.push(observer);
	}
	// 移除观察者
	unregisterObserver(observer) {
		const observerIndex = this.observerCollection.indexOf(observer);
		this.observerCollection.splice(observerIndex, 1);
	}
	// 通知观察者
	notifyObservers(subject) {
		const collection = this.observerCollection;
		const len = collection.length;
		if (len > 0) {
			for (let observer of collection) {
				observer.update(subject);
			}
		}
	}
}

// 观察者
class Observer {
	update() {}
}

// 表单的状态
class Todo extends Subject {
	constructor() {
		super();
		this.items = [];
	}
	// 添加todo
	addItem(item) {
		this.items.push(item);
		super.notifyObservers(this);
	}
}

// 列表渲染
class ListRender extends Observer {
	constructor(el) {
		super();
		this.el = document.getElementById(el);
	}
	// 更新列表
	update(todo) {
		super.update();
		const items = todo.items;
		this.el.innerHTML = items.map(text => `<li>${text}</li>`).join('');
	}
}

// 列表计数观察者
class CountObserver extends Observer {
	constructor(el) {
		super();
		this.el = document.getElementById(el);
	}
	// 更新计数
	update(todo) {
		this.el.innerText = `${todo.items.length}`;
	}
}

// 列表观察者
const listObserver = new ListRender('item-list');
// 计数观察者
const countObserver = new CountObserver('item-count');

const todo = new Todo();
// 添加列表观察者
todo.registerObserver(listObserver);
// 添加计数观察者
todo.registerObserver(countObserver);

// 获取todo按钮
const addBtn = document.getElementById('add-btn');
// 获取输入框的内容
const inputEle = document.getElementById('new-item');
addBtn.onclick = () => {
	const item = inputEle.value;
	// 判断添加的内容是否为空
	if (item) {
		todo.addItem(item);
		inputEle.value = '';
	}
};