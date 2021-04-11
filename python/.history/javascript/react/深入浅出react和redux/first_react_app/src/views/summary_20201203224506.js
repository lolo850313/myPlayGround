import React from 'react';
import React, { PropTypes } from 'react'

function Summary (props) {
    const {sum} = props
    return (
        <div>total count : { sum } </div>
    )
}
Summary.PropTypes = {
    value : PropTypes.number.isRequired
}

function mapStateToProps(state) {
    let sum = 0
    for (const key in state) {
        if (object.hasOwnProperty(key)) {
            sum += state[key];
            
        }
    }

    return { value : sum }
}
export default Summary