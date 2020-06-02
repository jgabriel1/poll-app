import React from 'react'

function Checkbox({ index, voteHandler, optionText, isVoted }) {
    return (
        <div className='checkboxContainer custom-control custom-checkbox mb-3' key={index}>
            <input
                className='custom-control-input'
                type='checkbox'
                id={`option${index}`}
                checked={isVoted}
                onChange={event => voteHandler(event, index)}
            />
            <label className='custom-control-label' htmlFor={`option${index}`}>{optionText}</label>
        </div>
    )
}

export default Checkbox
