import ReactDOM from 'react-dom';
import './index.css';
import Header from './Header';
import Content from './Content';
import {React, Component} from 'react'
import PropTypes from 'prop-types'


function createStore(reducer) {
  let state = null
  const listeners = []
  const subscribe = (listener) => listeners.push(listener)
  const getState = () => state
  const dispatch = (action) => {
    state = reducer(state, action)
    listeners.forEach( (listener) => listener())
  }
  dispatch({})
  return { getState, dispatch, subscribe }

}

const themeReducer = ( state, action) => {
  if(!state) {
    return {
      themeColor: 'red'
    }
  }

  switch (action.type) {
    case 'CHANGE_COLOR':
      return {
        ...state,
        themeColor : action.themeColor
      }  
    default:
      return state
  }
}

const store = createStore(themeReducer)

class Index extends Component {
  static childContextTypes = {
    store : PropTypes.object
  }
  //将store放入到context中
  getChildContext(){
    return { store }
  }

  render() {
      return (
          <div>
            <Header />
            <Content />
          </div>
      )
  }
}

ReactDOM.render(
    <Index />,
  document.getElementById('root')
);
