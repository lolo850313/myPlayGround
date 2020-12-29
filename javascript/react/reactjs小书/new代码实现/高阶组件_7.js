// 重构多层高阶组件

import React, { Component } from 'react'

//高阶组件，将ajax里name的数据取出，传入到子组件WrapperComponent中。达到复用效果。
wrapWithLoadData = (WrapperComponent, name) => {
    class LocalStorageActions extends Component {
        constructor () {
            super()
            this.state = { data : null}
        }

        componentWillMount () {
            let data = localStorage.getItem('name')

            try {
                this.setState( { data : JSON.parse(data) })
            } catch (error) {
                this.setState( { data })
            }
        }

        saveData () {
            try {
                localStorage.setItem(name, JSON.stringify(data))
            } catch (error) {
                localStorage.setItem(name, `${data}`)
            }
        }

        render() {
            return <WrapperComponent data={this.state.data} 
                saveData={this.saveData.bind(this)}
                {...this.props}
            />
        }
    }

    return LocalStorageActions
}


class InputWithUserName extends Component {
    render() {
        return <input value={this.props.data} />
    }
}


InputWithUserName = wrapWithLoadData(InputWithUserName, 'comments')

export default InputWithUserName