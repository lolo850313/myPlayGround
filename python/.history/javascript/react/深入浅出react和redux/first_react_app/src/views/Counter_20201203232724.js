import React,{ Component, PropTypes } from 'react';
import Counter from './Counter'

import * as Actions from '../Action.js'
import { connect } from 'react-redux';

const buttonStyle = {
    margin: '10px'
  }

function CounterContainer ({caption, onIncrement, onDecrement, value}) {
    return (
        <div>
            <button style={buttonStyle} onClick={onIncrement}>+</button>
            <button style={buttonStyle} onClick={onDecrement}>-</button>
            <span>{caption} count: {value}</span>
        </div>
    )
}
CounterContainer.contextTypes = {
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
}

export default CounterContainer