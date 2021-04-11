import React,{Component} from 'react';
import Counter from './Counter'
import Summary from './Summary'

const style = {
    margin: '20px'
  };
  
class ControlPanel extends Component {
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