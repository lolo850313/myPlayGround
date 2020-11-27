var events = require('events')
var emmiter = new events.EventEmitter()

emmiter.on('someEvent', function (arg1, arg2) {
    console.log('listener1', arg1, arg2)
})

emmiter.on('someEvent', function (arg1) {
    console.log('listener2', arg1)
})

emmiter.emit('someEvent','arg1 XXX', 'arg2 XXX')
