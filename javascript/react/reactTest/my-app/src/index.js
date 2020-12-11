import React ,{ Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Header extends Component {
  render() {
    const word = 'is good'
    return (
      <div>
        <h1 className={ word } htmlFor = { word }>react小书 { word }</h1>
      </div>
    )
  }
}


ReactDOM.render(
    <Header />,
  document.getElementById('root')
);
