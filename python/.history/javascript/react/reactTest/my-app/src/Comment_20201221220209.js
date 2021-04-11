import React ,{ Component }from 'react';

class Comment extends Component {
	// constructor(props){
	// 	super(props)
	// }

	static propTypes = {
		comment : PropTypes.object.isRequired
	}
	render() {
		return (
			<div className="comment">
				<div className="comment-user">
					<span>{this.props.comment.username} : </span>
				</div>
				<p>{this.props.comment.content}</p>
			</div>
		)
	}
}


export default Comment
