import React,{ PropTypes } from 'react';

import * as Actions from '../Action.js'
import { connect } from 'react-redux';
import { func } from 'prop-types';

const buttonStyle = {
    margin: '10px'
  }

function Counter ({caption, onIncrement, onDecrement, value}) {
    return (
        <div>
            <button style={buttonStyle} onClick={onIncrement}>+</button>
            <button style={buttonStyle} onClick={onDecrement}>-</button>
            <span>{caption} count: {value}</span>
        </div>
    )
}

function mapStateToProps(state, ownProps){
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

Counter.contextTypes = {
    caption : PropTypes.string.isRequired,
    onIncrement : PropTypes.func.isRequired,
    onDecrement : PropTypes.func.isRequired,
    value : PropTypes.number.isRequired,
}

export default connect(mapStateToProps, mapDispatchToProps)(Counter)