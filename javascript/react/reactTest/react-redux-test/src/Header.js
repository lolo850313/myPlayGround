import {React, Component} from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

class Header extends Component {
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

const mapStateToProps = (state) => {
    return {
        themeColor: state.themeColor,
    }
}

export default Header = connect(mapStateToProps)(Header)