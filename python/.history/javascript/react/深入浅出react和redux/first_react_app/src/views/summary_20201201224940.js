import React, from 'react';

function Summary () {
    render() {
        const sum = this.state.sum
        return (
            <div>total count : { sum } </div>
        )
    }
}

export default Summary