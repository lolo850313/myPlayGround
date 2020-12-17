import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class Clock extends Component {
	constructor() {
		super()
		this.state = {
			date : new Date()
		}
	}


	componentWillMount(){
		this.timer = setInterval( () => {
			this.setState({ date : new Date()})
		} , 1000)
	}
	
	componentWillUnmount(){
		clearInterval(this.timer)
	}

	render() {
		return (
			<div>
				<p>
					现在的时间是{this.state.date.toLocaleTimeString()}
				</p>
			</div>
		)
	}
}


class Index extends Component {
	constructor(){
		super()
		this.state = {
			isShowClock : true
		}
	}

	showClock() {
		this.setState({
			isShowClock : !this.state.isShowClock
		})
	}


	render(){
		return (
			<div>
				<button onClick={this.showClock.bind(this)}>显示或隐藏时钟</button>
				{ this.state.isShowClock ? <Clock /> : null }
			</div>
		)
	}

}


ReactDOM.render(
		<Index />,
	document.getElementById('root')
);
