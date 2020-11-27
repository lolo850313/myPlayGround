import { connect } from 'react-redux'
import Header from '../components/Header'

const mapStateProps =(state) => {
    return {
        themeColor: state.themeColor
    }
}

export default connect(mapStateProps)(Header)