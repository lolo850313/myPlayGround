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
	}
	render() {		
		return (
		<button onClick={this.handleClick}>{this.state.isLike? this.props.unLikeText : this.props.likeText}👍</button>
		)
	}
}

class Index extends Component {
	constructor() {
		super()
		this.state = {
			likeText : "已赞",
			unLikeText : "赞"
		}
	}

	handleClickOnChange () {
		this.setState({
			likeText: '取消',
			unLikeText : "点赞"
		})
	}
	render() {
		return (
				<div>
					<LikeButton 
					likeText={this.state.likeText} 
					unLikeText={this.state.unLikeText} 
					/>
					<div>
						<button onClick={this.handleClickOnChange.bind(this)} >修改 wordings</button>
					</div>
				</div>
		)
	}
}


ReactDOM.render(
		<Index />,
	document.getElementById('root')
);
