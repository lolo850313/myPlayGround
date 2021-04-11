import React from 'react';

const buttonStyle = {
    margin: '10px'
  }

function Counter(props) {
    const {caption, onIncrement, onDecrement, value} = props
    return (
        <div>
            <button style={buttonStyle} onClick={onIncrement}>
                +
            </button>
            <button style={buttonStyle} onClick={onDecrement}>
                -
            </button>
            <span>{caption} count : {value}</span>
        </div>
    )
}


export default Counter