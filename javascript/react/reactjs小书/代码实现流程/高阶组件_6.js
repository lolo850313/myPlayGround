// 多层高阶组件

//得到的组件会先去LocalStorage取数据，
//然后通过 props.data传给下一层组件，
//下一层用这个props.data通过Ajax去服务端取数据，
//然后再通过props.data把数据传给下一层，也就是InputWithUserName

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

//高阶组件，将父组件的data为作为ajax参数传入系统，得到相应的结果后更新state。
wrapWithLoadData = (WrapperComponent) => {
    class NewComponet extends Component {
        constructor () {
            super()
            this.state = { data : null}
        }

        // 传进来的 props.data 去服务器取数据。这时候修改 InputWithUserName
        componentWillMount () {
            ajax.get('/data/' + this.props.data, (data) => {
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
InputWithUserName = wrapWithAjaxData(InputWithUserName)
InputWithUserName = wrapWithLoadData(InputWithUserName, 'username')

export default InputWithUserName