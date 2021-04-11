import { createStore} from 'redux'
import reducer from './Reducer.js'

const counterValues = {
    'First' : 0,
    'Second' : 10,
    'Third' : 20
}

const stores = createStore(reducer, initValue)
)