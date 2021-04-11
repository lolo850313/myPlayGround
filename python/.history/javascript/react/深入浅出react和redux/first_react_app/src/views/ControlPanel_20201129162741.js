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
                <Counter caption="Second" />
                <Counter caption="Third" />
                <hr />
                <Summary />
            </div>
            
        )
    }
}
export default ControlPanel