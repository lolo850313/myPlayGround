import React,{ Component, PropTypes } from 'react';
import Counter from './Counter'

import * as Actions from '../Action.js'
import { connect } from 'react-redux';

const buttonStyle = {
    margin: '10px'
  }

function CounterContainer ({caption, onIncrement, onDecrement, value}) {
    return (
        <Counter caption={this.props.caption} 
        onIncrement={this.onIncrement} 
        onDecrement={this.onDecrement}
        value={this.state.value} />
    )
}
CounterContainer.contextTypes = {
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
    caption : PropTypes.string.isRequired,
}

export default CounterContainer