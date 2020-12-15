import React ,{ Component }from 'react';
import './index.css';
import CommentInput from './CommentInput'
import CommentList from './CommentList'

class CommentApp extends Component {
	constructor(props){
		super(props)
		this.state = {comments : []}
		this.handleSubmitComment = this.handleSubmitComment.bind(this)
	}

	handleSubmitComment(comment) {
		// const curComments = this.state.comments
		// this.setState({
		// 	comments : curComments.concat(comment)
		// })
	}
	
	render() {
		return (
				<div className='wrapper'>
					<CommentInput onSubmit={this.handleSubmitComment} />
					<CommentList />
				</div>
		)
	}
}


export default CommentApp
