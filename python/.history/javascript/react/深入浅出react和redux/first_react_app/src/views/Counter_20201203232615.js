import React,{ Component, PropTypes } from 'react';
import Counter from './Counter'

import * as Actions from '../Action.js'
import { connect } from 'react-redux';

const buttonStyle = {
    margin: '10px'
  }

function CounterContainer ({caption}) {
    return (
        <Counter caption={this.props.caption} 
        onIncrement={this.onIncrement} 
        onDecrement={this.onDecrement}
        value={this.state.value} />
    )
}
CounterContainer.contextTypes = {
    store : PropTypes.object
}

export default CounterContainer