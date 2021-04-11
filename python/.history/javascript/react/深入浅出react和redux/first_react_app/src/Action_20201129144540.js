import * as ActionTypes from "./ActionTypes";

export const increment = (counterCaption) => {
    return {
        type : ActionTypes.INCREMENT,
        counterCaption : counterCaption
    }
}

export const decrement = (counterCaption) => {
    AppDispatcher.dispatch({
        type : ActionTypes.DECREMENT,
        counterCaption : counterCaption
    })
}