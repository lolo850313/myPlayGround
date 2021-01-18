import React ,{ Component } from 'react';
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import CommentInput from '../components/CommentInput'
import { addComment } from '../reducers/comments'

class CommentInputContainer extends Component {
	static propTypes = {
		onSubmit : PropTypes.func,
		comments : PropTypes.array
	}

	constructor(){
		super()
		this.state = {
			username : "",
		}
		// this.handleUsernameChange = this.handleUsernameChange.bind(this)
		// this.handleContentChange = this.handleContentChange.bind(this)
		// this.handleSubmit = this.handleSubmit.bind(this)
	}

	componentWillMount(){
		this._loadUsername()
	}

	// componentDidMount(){
	// 	this.textarea.focus()
	// }

	_loadUsername() {
		const username = localStorage.getItem('username')
		if(username){
			this.setState({
				username
			})
		}
	
	}

	_saveUserName(username) {
		localStorage.setItem('username', username)
	}

	// handleUsernameBlur(event) {
	// 	this._saveUserName(event.target.value)
	// }

	// handleUsernameChange(event){
	// 	this.setState({
	// 		username : event.target.value
	// 	}) 
	// }

	// handleContentChange(event){
	// 	this.setState({
	// 		content : event.target.value
	// 	}) 
	// }

	// handleSubmit(){
	// 	if (this.props.onSubmit) {
	// 		this.props.onSubmit({
	// 			username : this.state.username, 
	// 			content : this.state.content,
	// 			createdTime : +new Date()
	// 		})
	// 	} 
		
	// 	this.setState({content : ""})
	// }



	// handleSubmitComment (comment) {
	// 	if(!comment) return
	// 	if(!comment.username) return alert('请输入用户名')
	// 	if(!comment.content) return alert('请输入评论')

	// 	let comments = this.state.comments
	// 	comments.push(comment)
	// 	this.setState({
	// 		comments : comments
	// 	})

	// 	this._saveComments(comments)
	// }

	handleSubmitComment ( comment ) {
		if (!comment) {
			return
		}
		if (!comment.username) {
			return alert('请输入用户名')
		}
		if (!comment.content) {
			return alert('请输入评论')
		}

		const { comments } = this.props
		console.log(comments,this.props)
		const newComments = [...comments, comment]
		localStorage.setItem('comments', JSON.stringify(newComments))

		//this.props.onSubmit是connect传进来的，会dispatch一个action增加评论
		if (this.props.onSubmit) {
			this.props.onSubmit(comment)
		}
	}


	render() {
		return (
			<CommentInput 
				username = {this.state.username}
				onUserNameInputBlur = { this._saveUserName.bind(this) }
				onSubmit = { this.handleSubmitComment.bind(this) }
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
		onSubmit: ( comment ) => {
			dispatch(addComment(comment))
		}
	}
}

export default connect(mapStateToProps, mapDispatchToProps)
(CommentInputContainer)
