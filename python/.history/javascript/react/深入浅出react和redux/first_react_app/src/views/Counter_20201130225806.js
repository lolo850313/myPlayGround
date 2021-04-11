import React,{ Component ,PropTypes } from 'react';

import * as Actions from '../Action.js'
import store from '../Store.js';

const buttonStyle = {
    margin: '10px'
  }

class Counter extends Component {
    render(){
        const {caption, onIncrement, onDecrement, value} = this.props
        return (
            <div>
                <button style={buttonStyle} onClick={this.onIncrement}>
                    +
                </button>
                <button style={buttonStyle} onClick={this.onDecrement}>
                    -
                </button>
                <span>{caption} count : {value}</span>
            </div>
        )
    }
}

Counter.propTypes = {
    caption : PropTypes.string.isRequired,
}

export default Counter