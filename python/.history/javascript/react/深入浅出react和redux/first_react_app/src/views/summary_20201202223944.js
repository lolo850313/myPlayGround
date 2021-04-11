import React from 'react';

function Summary (props) {
    const sum = props.sum
    return (
        <div>total count : { sum } </div>
    )
}

export default Summary