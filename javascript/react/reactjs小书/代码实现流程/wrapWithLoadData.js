// 将高阶组件的数据传入组件中

import React, { Component } from 'react'



export default (WrapperComponent, name) => {
    class NewComponet extends Component {
        constructor () {
            super()
            this.state = { data : null}
        }

        componentWillMount () {
            let data = localStorage.getItem(name)
            this.setState( { data })
        }

        render() {
            return <WrapperComponent data={this.state.data} />
        }
    }

    return NewComponent
}