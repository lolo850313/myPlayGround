import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class AutoFocusInput extends Component {
	componentDidMount(){
		this.input.focus()
	}

	render(){
		return (
			<div>
				<input ref={ (input) => this.input = input} />
			</div>
		)
	}

}


ReactDOM.render(
		<AutoFocusInput />,
	document.getElementById('root')
);
