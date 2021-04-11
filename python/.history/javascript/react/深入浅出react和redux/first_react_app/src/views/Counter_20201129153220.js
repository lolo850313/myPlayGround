import React,{Component} from 'react';
import PropTypes from 'prop-types';

class Counter extends Component {
    constructor(props){
        super(props)
        this.state = {
            count : props.initValue || 0
        }
        this.onClickIncrementButton = this.onClickIncrementButton.bind(this)
        this.onClickDecrementButton = this.onClickDecrementButton.bind(this)
    }

    
    onClickIncrementButton(){
        this.updateCount(true)
    }

    onClickDecrementButton(){
        this.updateCount(false)
    }

    updateCount(isIncrement){
        const previousValue = this.state.count
        const newValue = isIncrement ? previousValue + 1 : previousValue - 1
        this.setState({
            count : newValue
        })
        this.props.onUpdate(newValue, previousValue)
    }

    render(){
        // const {caption} = this.props
        return (
            <div>
                <button onClick={this.onClickIncrementButton}>
                    +
                </button>
                <button onClick={this.onClickDecrementButton}>
                    -
                </button>
                <span>{this.props.caption} count : {this.state.count}</span>
            </div>
        )
    }
}

Counter.propTypes = {
    caption : PropTypes.string.isRequired,
    initValue : PropTypes.number,
    onUpdate : PropTypes.func
}

Counter.defaultProps = {
    initValue : 0,
    onUpdate : f => f
}

export default Counter