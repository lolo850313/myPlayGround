import {React, Component} from 'react'
import PropTypes from 'prop-types'

export default class Header extends Component {
    static contextTypes = {
        store : PropTypes.object
    }

    render() {
        return (
            <div>
                <h1 style = {{ color : this.props.themeColor }}>react.js 小书</h1>
            </div>
        )
    }
}