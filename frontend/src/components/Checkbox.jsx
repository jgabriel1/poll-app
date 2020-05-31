import React from 'react'

function Checkbox({ index, voteHandler, optionText, isVoted }) {
    return (
        <div className='checkboxContainer' key={index}>
            <input
                type='checkbox'
                id={`option${index}`}
                checked={isVoted}
                onChange={event => voteHandler(event, index)}
            />
            <label htmlFor={`option${index}`}>{optionText}</label>
        </div>
    )
}

export default Checkbox
