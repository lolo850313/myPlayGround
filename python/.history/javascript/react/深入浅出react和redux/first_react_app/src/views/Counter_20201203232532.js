import React,{ Component, PropTypes } from 'react';
import Counter from './Counter'

import * as Actions from '../Action.js'
import { connect } from 'react-redux';

// const buttonStyle = {
//     margin: '10px'
//   }

class CounterContainer extends Component {
    constructor(props, context){
        super(props, context)
        
        this.onIncrement = this.onIncrement.bind(this)
        this.onDecrement = this.onDecrement.bind(this)
        
        this.getOwnState = this.getOwnState.bind(this)
        this.onChange = this.onChange.bind(this)

        this.state = this.getOwnState()
    }

    getOwnState () {
        return {
            value : this.context.store.getState()[this.props.caption]
        }
    }

    onIncrement(){
        store.dispatch(Actions.increment(this.props.caption))
    }

    onDecrement(){
        store.dispatch(Actions.decrement(this.props.caption))
    }
    onChange (){
        this.setState(this.getOwnState())
    }

    shouldComponentUpdate(nextProps, nextState) {
        return (nextProps.caption !== this.props.caption) || (nextState.value !== this.state.value)
    }

    componentDidMount() {
        store.subscribe(this.onChange)
    }

    componentWillUnmount() {
        store.unsubscribe(this.onChange)
    }

    render(){
        return (
            <Counter caption={this.props.caption} 
            onIncrement={this.onIncrement} 
            onDecrement={this.onDecrement}
            value={this.state.value} />
        )
    }
}
CounterContainer.contextTypes = {
    store : PropTypes.object
}

export default CounterContainer