var events = require('events')
var eventEmitter = new events.EventEmitter()

var listener1 = function l1() {
    console.log('监听器listener1执行');
}

var listener2 = function l2() {
    console.log('监听器listener2执行');
}

// addListener和on一样
eventEmitter.addListener('connection', listener1)
eventEmitter.on('connection', listener2)

var eventListeners = eventEmitter.listenerCount('connection')
console.log(eventListeners + "个监听器在connection上")

eventEmitter.emit('connection')

