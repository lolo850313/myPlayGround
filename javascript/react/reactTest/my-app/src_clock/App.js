import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: {
        username: null,
        password: null
      }
    }
  }
  handleChange(name, value) {
    let user = this.state.user;
    user[name] = value;
    this.setState({ user: user })
  }
  render() {
    return (
      <div>
        <h2>Basic PasswordBox</h2>
        <Form model={this.state.user} onChange={this.handleChange.bind(this)}>
          <div style={{ marginBottom: 20 }}>
            <TextBox name="username" value={this.state.user.username} placeholder="Username" iconCls="icon-man"></TextBox>
          </div>
          <div style={{ marginBottom: 20 }}>
            <PasswordBox name="password" value={this.state.user.password} placeholder="Password" iconCls="icon-lock"></PasswordBox>
          </div>
        </Form>
        <p>{JSON.stringify(this.state.user)}</p>
      </div>
    );
  }
}
 
export default App;