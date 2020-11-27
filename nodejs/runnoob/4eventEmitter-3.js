var events = require("events")
const { EventEmitter } = require("events")
const { listeners } = require("process")

var emitter = new events.EventEmitter()

var listener1 = function listener1() {
    console.log('监听器 listener1 执行')
}

var listener2 = function listener2() {
    console.log('监听器 listener2 执行')
}

// 事件监听on、addListener 没有区别
emitter.addListener('connection', listener1)
emitter.on('connection', listener2)

var eventListeners = EventEmitter.listenerCount('connection')

console.log(eventListeners + " 个监听器监听链接事件")

emitter.emit('connection')

emitter.removeListener('connection', listener1)
console.log('listener1 不在受监听')

emitter.emit('connection')

eventListeners = emitter.listenerCount('connection')
console.log(eventListeners + " 个监听器监听链接事件")

