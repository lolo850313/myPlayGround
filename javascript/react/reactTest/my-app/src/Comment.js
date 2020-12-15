import React ,{ Component }from 'react';

class Comment extends Component {
	// constructor(props){
	// 	super(props)
	// }
	render() {
		return (
			<div className="comment">
				<div className="comment-user">
					{this.props.comment.username} : {this.props.comment.content}
				</div>
			</div>
		)
	}
}


export default Comment
