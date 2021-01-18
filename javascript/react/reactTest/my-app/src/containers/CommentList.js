import React ,{ Component }from 'react';
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import CommentList from '../components/CommentList'
import { initComments, deleteComment} from '../reducers/comments'

class CommentListContainer extends Component {
	static propTypes = {
		comments : PropTypes.array,
		onDeleteComment: PropTypes.func,
		initComments : PropTypes.func
	}
	
	// static defaultProps = {
	// 	comments : []
	// }

	componentWillMount(){
		this._loadComments()
	}

	_loadComments() {
		//注意这里不能用const, 
		let comments = localStorage.getItem('comments')

		// if (comments) {
		// 	comments = JSON.parse(comments)

			
		// } else {
		// 	comments = []
		// }

		comments = comments ? JSON.parse(comments) : []
		this.props.initComments(comments)
	}

	// handleDeleteComment (index) {
	// 	let comments = this.state.comments
	// 	comments.splice(index, 1)
	// 	this.setState({
	// 		comments
	// 	})
	// 	this._saveComments(comments)
	// }

	handleDeleteComment(index) {
		const { comments } = this.props
		const newComments = [
			...comments.splice(0, index), 
			...comments.splice(index + 1)
		]

		localStorage.setItem('comments', JSON.stringify(newComments))
		if( this.props.onDeleteComment) {
			this.props.onDeleteComment(index)
		}
	}

	render() {
		return (
				<CommentList 
					comments = { this.props.comments}
					appDelete = { this.handleDeleteComment.bind(this)}
				/>
		)
	}
}

const mapStateToProps = (state) => {
	return {
		comments: state.comments
	}
}

const mapDispatchToProps = (dispatch) => {
	return {
		initComments: (comments) => {
			dispatch(initComments(comments))
		},
		onDeletecomment : (commentIndex) => {
			dispatch(deleteComment(commentIndex))
		}
	}
}

export default connect(mapStateToProps, mapDispatchToProps)(CommentListContainer)
