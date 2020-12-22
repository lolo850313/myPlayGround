import React ,{ Component }from 'react';
import PropTypes from "prop-types"

class Comment extends Component {
	// constructor(props){
	// 	super(props)
	// }

	// static propTypes = {
	// 	comment : this.propTypes.object.isRequired
	// }

	// constructor() {
	// 	super()
	// 	this.state = {timeString : ''}
	// }

	// componentWillMount () {
	// 	this._updateTimeString()
	// }


	// _updateTimeString (){
	// 	const comment = this.props.comment
	// }

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
