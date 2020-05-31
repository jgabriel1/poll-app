import React from 'react'

function Checkbox({ index, optionText, voted, handleSelection }) {
    return (
        <div className='checkboxContainer'>
            <input
                type='checkbox'
                id={`option${index}`}
                checked={voted}
                onChange={event => handleSelection(event)}
            />
            <label htmlFor={`option${index}`}>
                {optionText}
            </label>
        </div>
    )
}

export default Checkbox
