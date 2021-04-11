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

const mapStateToProps = (state, ownProps) => {
    return {
        value : state[ownProps.caption]
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onIncrement: () => {
            dispatch(Actions.increment(ownProps.caption))
        },
        onDecrement: () => {
            dispatch(Actions.decrement(ownProps.caption))
        }
    }
}
CounterContainer.contextTypes = {
    caption : PropTypes.string.isRequired,
    onIncrement : PropTypes.func.isRequired,
    onDecrement : PropTypes.func.isRequired,
    value : PropTypes.number.isRequired,
}

export default CounterContainer