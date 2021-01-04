// 将高阶组件的数据传入组件中

// InputWithUserName的功能需求是
//挂载的时候从LocalStorage里面加载username字段作为<input />的value值

import React, { Component } from 'react'

//高阶组件，将ajax里name的数据取出，传入到子组件WrapperComponent中。达到复用效果。
wrapWithAjaxData = (WrapperComponent, name) => {
    class NewComponet extends Component {
        constructor () {
            super()
            this.state = { data : null}
        }

        componentWillMount () {
            ajax.get('/data/'+name, (data) => {
                this.setState( { data })
            })
        }

        render() {
            return <WrapperComponent data={this.state.data} />
        }
    }

    return NewComponent
}

class InputWithUserName extends Component {
    render() {
        return <input value={this.props.data} />
    }
}

//使用高阶组件将localStorage里存储的username的数据传入InputWithUserName
InputWithUserName = wrapWithAjaxData(InputWithUserName, 'username')


export default InputWithUserName