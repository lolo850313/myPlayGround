import React ,{ Component }from 'react';
import ReactDOM from 'react-dom';
import './index.css';

const users = [
	{ username: 'Jerry', age: 21, gender: 'male' },
	{ username: 'Tomy', age: 22, gender: 'male' },
	{ username: 'Lily', age: 19, gender: 'female' },
	{ username: 'Lucy', age: 20, gender: 'female' }
  ]

class User extends Component {
	render() {
		const user = this.props.user
		return (
			<div key={this.props.id}>
				<div>姓名 : {user.username}</div>
				<div>年龄 : {user.age}</div>
				<div>性别 : {user.gender}</div>
				<hr/>
			</div>
		)
	}
}
class Index extends Component {
	render() {
		return (
				<div>
					{users.map( (user, id)=> 
							<User user={user} key={id} />
						)}
				</div>
		)
	}
}


ReactDOM.render(
		<Index />,
	document.getElementById('root')
);
