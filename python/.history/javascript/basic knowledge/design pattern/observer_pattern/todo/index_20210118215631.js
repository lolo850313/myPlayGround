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