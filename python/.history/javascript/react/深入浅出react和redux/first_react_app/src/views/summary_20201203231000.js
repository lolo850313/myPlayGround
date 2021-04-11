import React from 'react';

function Summary (props) {
    const { sum } = props
    return (
        <div>total count : { props.sum } </div>
    )
}


export default Summary