import React, { Component } from 'react'
import PropTypes from 'prop-types'

class CommentInput extends Component {
    static propTypes = {
        username: PropTypes.any,
        onSubmit: PropTypes.func,
        onUserNameInputBlur: PropTypes.func
    }

    static defaultProps = {
        username : ''
    }

    constructor (props){
        super(props)
        this.state = {
            username : props.username,
            content : "",
        }
    }
    componentDidMount() {
        this.refs.qq.focus()
    }

    // componentWillMount () {
    //     this._loadUsername()
    // }

    // _loadUsername() {
    //     const username = localStorage.getItem('username')
    //     if (username){
    //         this.setState({username})
    //     }
    // }
    // _saveUsername(username){
    //     localStorage.setItem('username', username)
    // }

    
    handleUsernameBlur (event){
        if (this.props.onUserNameInputBlur) {
            this.props.onUserNameInputBlur(event.target.value)
        }
        // this._saveUsername(event.target.value)
    }

    handleUsernameChange (event){
        this.setState({
            username: event.target.value
        })
    }

    handleContentChange (event){
        this.setState({
            content: event.target.value
        })
    }

    

    handleSubmit (){
        if (this.props.onSubmit) {
            this.props.onSubmit({
                username : this.state.username, 
                content : this.state.content,
                createdTime : +new Date()})
        }
        this.setState({content : ''})
    }

    render () {
        return (
            <div className="comment-input">
                <div className="comment-field">
                    <span className="comment-name">用户名:</span>
                    <div className="comment-field-input">
                        <input 
                        value={this.state.username} 
                        onChange={this.handleUsernameChange.bind(this)}
                        onBlur={this.handleUsernameBlur.bind(this)} />
                    </div>
                </div>
                <div className="comment-field">
                    <span className="comment-name">评论内容:</span>
                    <div className="comment-field-input">
                        <textarea 
                            ref="qq"
                            value={this.state.content} 
                            onChange={this.handleContentChange.bind(this)} />
                    </div>
                </div>
                <div className="comment-button">
                    <button onClick={this.handleSubmit.bind(this)} >
                        发布
                    </button>
                </div>
            </div>
        )
    }
}

export default CommentInput