import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import { Layout, Menu } from 'antd'
import { 
	MenuUnfoldOutlined, 
	MenuFoldOutLined, 
	UserOutLined, 
	VideoCameraOutLined, 
	UploadOutLined } from '@ant-design/icons'

const { Header, Sider, Content } = Layout

class App extends React.Component {
	state = {
		collapsd : false
	}

	toggle = () => {
		this.setState({
			collapsd : !this.state.collapsd,
		})
	}

	render() {
		return (
			<Layout>
				<Sider>
					<div className='logo' />
				</Sider>
				<Layout>
					<Header>Header</Header>
					<Content>Content</Content>
				</Layout>
			</Layout>
		)
	}
}

export default App;
