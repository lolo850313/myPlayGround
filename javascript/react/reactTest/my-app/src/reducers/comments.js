//action type
const INIT_COMMENTS = 'INIT_COMMENTS'
const ADD_COMMENT = 'ADD_COMMENT'
const DELETE_COMMENT = 'DELETE_COMMENT'

//reducer
export default function commentsReducer (state, action) {
    if (!state) {
        state = { comments : [] }
    }

    switch (action.type) {
        case INIT_COMMENTS:
            return { comments : action.comment}

        case ADD_COMMENT:
            return { 
                comments : [...state.comments, action.comment]
            }
        case DELETE_COMMENT:
            return { 
                comments : [
                    ...state.comments.slice(0, action.commentIndex), 
                    ...state.comments.slice(action.commentIndex + 1),
                ]
            }
    
        default:
            return state;
    }
}

export const initComments = (comments) => {
    return { type: INIT_COMMENTS, comments}
}

export const addComment = (comment) => {
    return { type : ADD_COMMENT, comment}
}

export const deleteComment = (commentIndex) => {
    return { type : DELETE_COMMENT, commentIndex}
}