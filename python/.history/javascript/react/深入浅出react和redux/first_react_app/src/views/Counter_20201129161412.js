import React,{ PropTypes } from 'react';
import { connect } from 'react-redux';
import * as Actions from '../Action.js'
import stores from '../Store.js';

const buttonStyle = {
    margin: '10px'
  }

class Counter extends Component {
    constructor(props){
        super(props)
        
        this.onClickIncrementButton = this.onClickIncrementButton.bind(this)
        this.onClickDecrementButton = this.onClickDecrementButton.bind(this)
        this.onChange = this.onChange.bind(this)

        this.state = this.getOwnState()
    }

    getOwnState () {
        return {
            value : stores.getState()[this.props.caption]
        }
    }
    onIncrementButton(){
        stores.dispatch(Actions.increment(this.props.caption))
    }

    onDecrementButton(){
        stores.dispatch(Actions.decrement(this.props.caption))
    }
    onchange (){
        this.setState(this.getOwnState())
    }

    componentDidMount() {
        stores.subscribe(this.onChange)
    }

    componentWillUnmount() {
        stores.unsubscribe(this.onChange)
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