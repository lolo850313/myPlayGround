import React ,{ Component }from 'react';
import './index.css';
import CommentInput from './CommentInput'
import CommentList from './CommentList'

class CommentApp extends Component {
	constructor(props){
		super(props)
		this.state = {
			comments : []
		}
		this.handleSubmitComment = this.handleSubmitComment.bind(this)
	}

	handleSubmitComment(comment) {
		console.log(comment)
		if(!comment) return 
		if(!comment.usename) return alert('请输入用户名')

		if(!comment.content) return alert('请输入评论')

		const curComments = this.state.comments
		curComments.push(comment)
		this.setState({
			comments : curComments
		})
	}
	
	render() {
		return (
				<div className='wrapper'>
					<CommentInput onSubmit={this.handleSubmitComment} />
					<CommentList comments={this.state.comments} />
				</div>
		)
	}
}


export default CommentApp
