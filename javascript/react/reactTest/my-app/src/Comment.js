import React ,{ Component }from 'react';
import PropTypes from 'prop-types'

class Comment extends Component {
	static propTypes = {
		comment : PropTypes.object.isRequired,
		onDeletedComment: PropTypes.func,
		index: PropTypes.number
	}

	constructor() {
		super()
		this.state = {timeString : ''}
		this.handleDeleteComment = this.handleDeleteComment.bind(this)
	}

	componentWillMount () {
		this._updateTimeString()
		this._timer = setInterval(
			this._updateTimeString.bind(this),
			5000
		)
	}

	componentWillUnmount() {
		clearInterval(this._timer)
	}


	_updateTimeString (){
		const comment = this.props.comment
		const duration = (+Date.now() - comment.createdTime) / 1000
		this.setState({
			timeString: duration > 60 ? 
			`${Math.round(duration / 60)} 分钟前` 
			: `${Math.round(Math.max(duration, 1))} 秒前` 
		})
	}

	//var str = "Doe, John";
	// str.replace(/(\w+)\s*, \s*(\w+)/, "$2 $1");
	// 说明：$1,$2上就是按顺序对应小括号里面的小正则 捕获到的内容。
	 
	_getProcessedContent (content) {
		content =  content.replace(/&/g, "&amp;")
		.replace(/</g, "&lt;")
		.replace(/>/g, "&gt;")
		.replace(/"/g, "&quot;")
		.replace(/'/g, "&#039;")
		.replace(/`([\S\s]+?)`/g, '<code>$1</code>')

		console.log(content)
		
		return content
	}

	handleDeleteComment() {
		if(this.props.listDelete){
			this.props.listDelete(this.props.index)
		}
	}

	render() {
		const { comment } = this.props
		return (
			<div className="comment">
				<div className="comment-user">
					<span>{comment.username} : </span>
				</div>
				<p dangerouslySetInnerHTML={{ 
					__html: this._getProcessedContent(comment.content)
					}} />
				<span className='comment-createdtime'>
					{this.state.timeString}
				</span>
				<span className='comment-delete'
					onClick={this.handleDeleteComment}
				>
					删除
				</span>
			</div>
		)
	}
}


export default Comment
