class Subject {
    constructor() {
        this.observerCollection
    }
    
    registerObserver(observer) {
        this.observerCollection.push(observer)
    }
}