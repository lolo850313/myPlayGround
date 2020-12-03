import {PropTypes, Component} from 'react'

class Provider extends Component {
    getChilderContext() {
        return {
            store : this.props.store
        }
    }

    render () {
        return this.props.children
    }
}
export default Provider