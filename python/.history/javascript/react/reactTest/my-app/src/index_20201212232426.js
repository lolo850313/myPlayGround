import React ,{ Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class LikeButton extends Component {
	constructor(props) {
		super(props)
		this.state = {
			isLike : true
		}
		this.handleClick = this.handleClick.bind(this)
	}
	handleClick() {
		this.setState({
			isLike : !this.state.isLike
		})
		this.setState((e) => {
			return {count : 0}
		})
		console.log(this.state.count)
		this.setState((e) => {
			return {count : e.count + 1}
		})
		console.log(this.state.count)
		this.setState((e) => {
			return {count : e.count + 2}
		})
		console.log(this.state.count)
	}
	render() {
		return (
		<button onClick={this.handleClick}>{this.state.isLike? this.props.unLikeText : this.props.likeText}👍</button>
		)
	}
}

class Index extends Component {
	render() {
		return (
				<div>
					<LikeButton LikeText='已赞' unLikeText='赞' />
					<LikeButton />
				</div>
		)
	}
}


ReactDOM.render(
		<Index />,
	document.getElementById('root')
);
