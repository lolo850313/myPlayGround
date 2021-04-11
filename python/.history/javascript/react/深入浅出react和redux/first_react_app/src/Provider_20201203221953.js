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
Provider.childContextTypes = {
    store : PropTypes.object
}
export default Provider