import React, { Component } from 'react';

import store from '../Store.js';

class Summary extends Component {
    constructor(props){
        super(props)

        this.onChange = this.onChange.bind(this)

        this.state = this.getOwnState()
    }

    onChange() {
        this.setState(this.getOwnState())
    }

    getOwnState() {
        const state = store.getState()
    }
}