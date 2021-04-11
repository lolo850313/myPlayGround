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
                <Counter caption="First" />
                <Counter caption="Second" initValue={this.initValue[1]} />
                <Counter caption="Third" initValue={this.initValue[2]} />
                <hr />
                <Summary />
            </div>
            
        )
    }
}
export default ControlPanel