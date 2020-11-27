import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { connect} from 'react-redux'
import CommentInput from '../components/CommentInput'
import { addComment } from '../reducers/comments'


class CommentInputContainer  extends Component {
    static propTypes = {
        comments: PropTypes.array,
        onSubmit: PropTypes.func,
    }

    constructor (){
        super()
        this.state = {
            username : "",
        }
    }
    // componentDidMount() {
    //     this.refs.qq.focus()
    // }

    componentWillMount () {
        this._loadUsername()
    }

    _loadUsername() {
        const username = localStorage.getItem('username')
        if (username){
            this.setState({username})
        }
    }
    _saveUsername(username){
        localStorage.setItem('username', username)
    }

    
    // handleUsernameBlur (event){
    //     if (this.props.onUserNameInputBlur) {
    //         this.props.onUserNameInputBlur(event.target.value)
    //     }
    //     // this._saveUsername(event.target.value)
    // }

    // handleUsernameChange (event){
    //     this.setState({
    //         username: event.target.value
    //     })
    // }

    // handleContentChange (event){
    //     this.setState({
    //         content: event.target.value
    //     })
    // }

    

    handleSubmitComment (comment){
        if(!comment) return
        if(!comment.username) return alert("用户名")
        if(!comment.content) return alert("评论内容")
        
        const { comments } = this.props
        console.log(comments)
        const newComments = [...comments, comment]

        localStorage.setItem('comments', JSON.stringify(newComments))
        if (this.props.onSubmit) {
            this.props.onSubmit(comment)
        }
        // this.setState({content : ''})
    }

    render () {
        return (
            // <div className="comment-input">
            //     <div className="comment-field">
            //         <span className="comment-name">用户名:</span>
            //         <div className="comment-field-input">
            //             <input 
            //             value={this.state.username} 
            //             onChange={this.handleUsernameChange.bind(this)}
            //             onBlur={this.handleUsernameBlur.bind(this)} />
            //         </div>
            //     </div>
            //     <div className="comment-field">
            //         <span className="comment-name">评论内容:</span>
            //         <div className="comment-field-input">
            //             <textarea 
            //                 ref="qq"
            //                 value={this.state.content} 
            //                 onChange={this.handleContentChange.bind(this)} />
            //         </div>
            //     </div>
            //     <div className="comment-button">
            //         <button onClick={this.handleSubmit.bind(this)} >
            //             发布
            //         </button>
            //     </div>
            // </div>
            <CommentInput username={this.state.username}
                onUserNameInputBlur={this._saveUsername.bind(this)}
                onSubmit={this.handleSubmitComment.bind(this)}
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
        onSubmit: (comment) => {
            dispatch(addComment(comment))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(CommentInputContainer)