import React,  { Component } from 'react'
import PropTypes from 'prop-types'

export default class ThemeSwitch extends Component {
    static contextTypes = {
        store : PropTypes.object,
        onSwitchColor : PropTypes.func
    }

    handleSwitchColor(color) {
        if(this.props.onSwitchColor) {
            this.props.onSwitchColor(color)
        }
    }

    render() {
        return (
            <div>
                <button 
                    style={{ color : this.props.themeColor }}
                    onClick={this.handleSwitchColor.bind(this, 'red')}
                    >red</button>
                <button 
                    style={{ color : this.props.themeColor }}
                    onClick={this.handleSwitchColor.bind(this,'blue')}
                >blue</button>
            </div>
        )
    }
}