class myEventEmitter {
    constructor(){
        this.eventMap = {}
    }

    //type事件名称
    on(type, handler) {
        if(!handler instanceof Function){
            throw new Error("请传入一个函数")
        }
        if(!this.eventMap[type]){
            this.eventMap[type] = []
        }

        this.eventMap[type].push(handler)
    }

    emit(type, params) {
        if (this.eventMap[type]) {
            this.eventMap[type].forEach( (handler, index) => {
                handler(params)
            });
        }
    }

    off(type, handler) {
        if(this.eventMap[type]) {
            this.eventMap[type].splice(this.eventMap[type].indexOf(handler)>>>0, 1)
        }
    }
}

const myEvent = new myEventEmitter()

const testHandler = function (params) {
    console.log(`test 事件触发， testHandler接受到的参数是${params}`)
}

myEvent.on("test", testHandler)

myEvent.emit("test", "newState")