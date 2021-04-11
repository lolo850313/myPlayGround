import React, { Component, PropTypes } from 'react';
import Summary from './Summary'
import store from '../Store.js';

class SummaryContainer extends Component {
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
        return (
            <Summary  sum={this.state.sum} />
        )
    }
}

SummaryContainer.PropTypes = {
    value : PropTypes.number.isRequired
}
function mapStateToProps(state) {
    let sum = 0
    for (const key in state) {
        if (object.hasOwnProperty(key)) {
            sum += state[key];
            
        }
    }

    return { value : sum }
}
export default connect(mapStateToProps)(SummaryContainer)