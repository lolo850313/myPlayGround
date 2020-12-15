import React ,{ Component }from 'react';

class Comment extends Component {
	constructor(props){
		super(props)
	}
	render() {
		return (
				<div key={this.props.key} >
					Comment
				</div>
		)
	}
}


export default Comment
