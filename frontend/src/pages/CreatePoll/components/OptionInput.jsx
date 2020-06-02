import React from 'react'

function OptionInput({ value, index, changeHandler }) {
    return (
        <div className='optionContaier input-group mb-3' key={index}>
            <div className='input-group-prepend'>
                <label className='input-group-text' htmlFor={`option${index}`}>
                    {`${index + 1}`}
                </label>
            </div>
            <input
                type='text'
                className='form-control'
                id={`option${index}`}
                value={value}
                onChange={changeHandler}
            />
        </div>
    )
}

export default OptionInput
