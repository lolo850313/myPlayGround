//手动实现一个eventEmitter
class eventEmitter{
    constructor() {
        this.events = Object.create(null)
    }
    on(name, fn) {
        if(!this.events[name]) {
            this.events[name] = []
        }
        this.events[name].push(fn)
        return this
    }

    emit(name, ...args) {
        if(!this.events[name]) {
            return this
        }
        const fns = this.events[name]
        fns.forEach(fn => fn.call(this, ...args))
        return this
    }

    off(name, fn)
}