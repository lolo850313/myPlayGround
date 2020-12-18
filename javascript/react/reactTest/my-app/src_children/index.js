import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Card extends Component {
	render(){
		return (
			<div className="card">
				//整个children引用
				<div className="card-content">
					{this.props.children}
				</div>

				//以数组形式单个引用
				<div className="card-content">
					{this.props.children[4]}
				</div>
				<div className="card-content">
					{this.props.children[3]}
				</div>
				<div className="card-content">
					{this.props.children[2]}
				</div>
			</div>
		)
	}

}


ReactDOM.render(
		<Card>
			<h2>childern1</h2>
			<div>childern2</div>
			childern3<input value="children4"/>
			childern5
		</Card> ,
	document.getElementById('root')
);
