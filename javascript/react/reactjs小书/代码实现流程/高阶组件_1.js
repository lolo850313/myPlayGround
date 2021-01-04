import React, { Component } from 'react'

export default (WrapperComponent) => {
    class NewComponet extends Component {
        render() {
            return <WrapperComponent />
        }
    }

    return NewComponent
}