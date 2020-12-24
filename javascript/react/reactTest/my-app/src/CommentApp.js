import React ,{ Component }from 'react';
import CommentInput from './CommentInput'
import CommentList from './CommentList'

class CommentApp extends Component {
	constructor(){
		super()
		this.state = {
			comments : []
		}
		this.handleSubmitComment = this.handleSubmitComment.bind(this)
		this.handleDeleteComment = this.handleDeleteComment.bind(this)
	}


	componentWillMount(){
		this._loadComments()
	}

	_loadComments() {
		//注意这里不能用const, 
		let comments = localStorage.getItem('comments')

		if (comments) {
			comments = JSON.parse(comments)

			this.setState({ comments })
		}
	}

	_saveComments(comments) {
		localStorage.setItem('comments', JSON.stringify(comments))
	}

	handleSubmitComment (comment) {
		if(!comment) return
		if(!comment.username) return alert('请输入用户名')
		if(!comment.content) return alert('请输入评论')

		let comments = this.state.comments
		comments.push(comment)
		this.setState({
			comments : comments
		})

		this._saveComments(comments)
	}

	handleDeleteComment (index) {
		console.log(index)
	}
	
	render() {
		return (
				<div className='wrapper'>
					<CommentInput onSubmit={this.handleSubmitComment} />
					<CommentList comments={this.state.comments} appDelete={this.handleDeleteComment}/>
				</div>
		)
	}
}


export default CommentApp
