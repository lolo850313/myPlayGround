import React,{ Component ,PropTypes } from 'react';

const buttonStyle = {
    margin: '10px'
  }

class Counter extends Component {
    render(){
        const {caption, onIncrement, onDecrement, value} = this.props
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
}

export default Counter