var events = require('events')
var emmiter = new events.EventEmitter()

var listener1 = function listener1() {
    console.log('监听器1 执行')
}

var listener2 = function listener2() {
    console.log('监听器2 执行')
}


emmiter.addListener('connection', listener1)

emmiter.on('connection', listener2)

var eventListeners = events.EventEmitter.listenerCount(emmiter,'connection')

console.log(eventListeners + '个监听连接事件')

emmiter.emit('connection')

emmiter.removeListener('connetion',listener1)

console.log('listener1 不在受监听')

emmiter.emit('connetion')

eventListeners = events.EventEmitter.listenerCount(emmiter, 'connection')

console.log(eventListeners + '个监听器监听连接事件')

console.log('Program end!')