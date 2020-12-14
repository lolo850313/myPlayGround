import React ,{ Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const users = [
	{ username: 'Jerry', age: 21, gender: 'male' },
	{ username: 'Tomy', age: 22, gender: 'male' },
	{ username: 'Lily', age: 19, gender: 'female' },
	{ username: 'Lucy', age: 20, gender: 'female' }
  ]

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
