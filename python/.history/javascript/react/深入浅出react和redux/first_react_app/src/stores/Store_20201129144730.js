import { createStore} from 'redux'
import reducer from './Reducer.js'
const counterValues = {
    'First' : 0,
    'Second' : 10,
    'Third' : 20
}

const CounterStores = Object.assign({}, EventEmitter.prototype,{
        getCounterValues : function(){
                return counterValues
            },
        emitChange:function(){
                this.emit(CHANGE_EVENT)
            },
        addChangeListener: function(callback){
            this.on(CHANGE_EVENT, callback)
        },
        removeChangeListener : function(callback){
            this.removeListener(CHANGE_EVENT, callback)
        }
    }
)