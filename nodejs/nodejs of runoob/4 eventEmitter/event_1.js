var events = require('events')
var event = new events.EventEmitter()

event.on('someEvent', function () {
    console.log('SomeEvent emit!')
})

setTimeout(function () {
    event.emit('someEvent')
}, 1000)
