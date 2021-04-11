import React from 'react';

function Summary ({ value }) {
    return (
        <div>total count : { value } </div>
    )
}

function mapStateToProps(state) {
    let sum = 0
    for (const key in state) {
        if (object.hasOwnProperty(key)) {
            sum += state[key];
            
        }
    }

    return { value : sum }
}
export default connect(mapStateToProps)(Summary)