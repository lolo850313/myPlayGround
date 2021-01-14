import {React, Component} from 'react'
import ThemeSwitch from './ThemeSwitch';
import PropTypes from 'prop-types'
import { connect } from 'react-redux'

class Content extends Component {
    static contextTypes = {
        themeColor : PropTypes.string
    }

    render() {
        return (
            <div>
                <p style={{ color : this.props.themeColor}}>react.js 小书内容</p>
                <ThemeSwitch />
            </div>
        )
    }
}
const mapStateToProps = (state) => {
    return {
        themeColor: state.themeColor
    }
}

Content = connect(mapStateToProps)(Content)
export default Content