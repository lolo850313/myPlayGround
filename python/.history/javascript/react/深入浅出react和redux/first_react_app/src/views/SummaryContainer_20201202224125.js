import React, { Component } from 'react';
import Summary from './Summary'
import store from '../Store.js';

class Summary extends Component {
    constructor(props){
        super(props)

        this.onChange = this.onChange.bind(this)

        this.state = this.getOwnState()
    }

    onChange() {
        this.setState(this.getOwnState())
    }

    getOwnState() {
        const state = store.getState()
        let sum = 0
        for (const key in state){
            if(state.hasOwnProperty(key)) {
                sum += state[key]
            }
        }

        return {sum : sum}
    }

    shouldComponentUpdate(nextProps, nextState){
        return nextState.sum !== this.state.sum
    }

    componentDidMount() {
        store.subscribe(this.onChange)
    }

    componentWillUnmount() {
        store.unSubscribe(this.onChange)
    }

    render() {
        const sum = this.state.sum
        return (
            <Summary  sum={sum} />
        )
    }
}

export default Summary