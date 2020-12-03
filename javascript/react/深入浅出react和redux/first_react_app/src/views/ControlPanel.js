import React,{Component} from 'react';
import CounterContainer from './CounterContainer'
import SummaryContainer from './SummaryContainer'

const style = {
    margin: '20px'
  };
  
class ControlPanel extends Component {
    render() {
        return (
            <div style={style}>
                <CounterContainer caption="First"  />
                <CounterContainer caption="Second" />
                <CounterContainer caption="Third"  />
                <hr />
                <SummaryContainer />
            </div>
            
        )
    }
}
export default ControlPanel