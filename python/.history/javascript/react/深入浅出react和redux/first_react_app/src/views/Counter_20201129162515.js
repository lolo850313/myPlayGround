import React,{ PropTypes } from 'react';
import { connect } from 'react-redux';
import * as Actions from '../Action.js'
import store from '../Store.js';

const buttonStyle = {
    margin: '10px'
  }

class Counter extends Component {
    constructor(props){
        super(props)
        
        this.onIncrementButton = this.onIncrementButton.bind(this)
        this.onDecrementButton = this.onDecrementButton.bind(this)
        this.onChange = this.onChange.bind(this)

        this.state = this.getOwnState()
    }

    getOwnState () {
        return {
            value : store.getState()[this.props.caption]
        }
    }
    onIncrementButton(){
        store.dispatch(Actions.increment(this.props.caption))
    }

    onDecrementButton(){
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

Counter.defaultProps = {
    initValue : 0,
    onUpdate : f => f
}

export default Counter