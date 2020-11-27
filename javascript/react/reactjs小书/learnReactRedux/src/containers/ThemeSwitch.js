import { connect } from 'react-redux'
import ThemeSwitch from '../components/ThemeSwitch'

const mapStateProps = (state) => {
    return {
        theme : state.themeColor
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        onSwitchColor: (color) => {
            dispatch({ type :'CHANGE_COLOR' , themeColor: color})
        }
    }
}

export default connect(mapStateProps, mapDispatchToProps)(ThemeSwitch)