import React,{ Component ,PropTypes } from 'react';

import * as Actions from '../Action.js'
import store from '../Store.js';

const buttonStyle = {
    margin: '10px'
  }

class Counter extends Component {
    constructor(props){
        super(props)
        
        this.onIncrement = this.onIncrement.bind(this)
        this.onDecrementButton = this.onDecrementButton.bind(this)
        this.onChange = this.onChange.bind(this)
        this.getOwnState = this.getOwnState.bind(this)
        this.state = this.getOwnState()
    }

    getOwnState () {
        return {
            value : store.getState()[this.props.caption]
        }
    }
    onIncrement(){
        store.dispatch(Actions.increment(this.props.caption))
    }

    onDecrement(){
        store.dispatch(Actions.decrement(this.props.caption))
    }
    onchange (){
        this.setState(this.getOwnState())
    }

    componentDidMount() {
        store.subscribe(this.onChange)
    }

    componentWillUnmount() {
        store.unsubscribe(this.onChange)
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
        const {caption} = this.props
        const value = this.state.value
        return (
            <div>
                <button style={buttonStyle} onClick={this.onIncrementButton}>
                    +
                </button>
                <button style={buttonStyle} onClick={this.onDecrementButton}>
                    -
                </button>
                <span>{caption} count : {value}</span>
            </div>
        )
    }
}

Counter.propTypes = {
    caption : PropTypes.string.isRequired,
}

export default Counter