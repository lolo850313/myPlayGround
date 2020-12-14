import React ,{ Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';

class LikeButton extends Component {
	static defaultProps = {
		likedText : '取消',
		unLikedText : '点赞'
	}
	constructor() {
		super()
		this.state = {
			isLike : false
		}
		this.handleClick = this.handleClick.bind(this)
	}
	handleClick() {
		this.setState({
			isLike : !this.state.isLike
		})

		if(this.props.onClick){
			this.props.onClick()
		}
	}
	render() {		
		return (
		<button onClick={this.handleClick}>
			{this.state.isLike? this.props.likedText : this.props.unLikedText👍}
		</button>
		)
	}
}

class Index extends Component {
	render() {
		return (
				<div>
					<LikeButton 
					 likedText='已赞'
					 unLikedText = '赞'
					 onClick = { ()=> console.log("clicked")}
					 />
					<LikeButton />
				</div>
		)
	}
}


ReactDOM.render(
		<Index />,
	document.getElementById('root')
);
