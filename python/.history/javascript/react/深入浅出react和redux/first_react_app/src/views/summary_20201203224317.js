import React from 'react';
import React, { PropTypes } from 'react'

function Summary (props) {
    const {sum} = props
    return (
        <div>total count : { sum } </div>
    )
}

export default Summary