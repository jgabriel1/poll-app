import React from 'react'

function OptionInput({ index }) {
    return (
        <div className='optionContainer'>
            <label htmlFor={`option${index}`}>{`${index + 1}. `}</label>
            <input type='text' name={`option${index}`} id={`option${index}`} />
        </div>
    )
}

export default OptionInput
