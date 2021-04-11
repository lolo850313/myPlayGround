import React,{Component} from 'react';
import Counter from './Counter'
import Summary from './Summary'

class ControlPanel extends Component {
    constructor(props){
        super(props)
        this.onCounterUpdate = this.onCounterUpdate.bind(this)

        this.initValue = [0, 10 ,20]
        const initSum = this.initValue.reduce((a, b) => a+b, 0)
        this.state = {
            sum : initSum
        }
    }

    onCounterUpdate(newValue, previousValue) {
        const valueChange = newValue - previousValue
        this.setState({
            sum : this.state.sum + valueChange
        })
    }

    render() {
        return (
            <div>
                <Counter onUpdate={this.onCounterUpdate} caption="First" />
                <Counter onUpdate={this.onCounterUpdate} caption="Second" initValue={this.initValue[1]} />
                <Counter onUpdate={this.onCounterUpdate} caption="Third" initValue={this.initValue[2]} />
                <hr />
                <div>Total count : {this.state.sum}</div>
            </div>
            
        )
    }
}
export default ControlPanel