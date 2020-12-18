import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Card extends Component {
	render(){
		return (
			<div className="card">
				<div className="card-content">
					{this.props.children}
				</div>
			</div>
		)
	}

}


ReactDOM.render(
		<Card>
			<h2>React.js 小书</h2>
			<div>开源、免费、专业、简单</div>
			订阅: <input />
		</Card> ,
	document.getElementById('root')
);
