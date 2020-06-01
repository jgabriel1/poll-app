import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'

import api from '../services/api'

function CreatePoll() {
    const [question, setQuestion] = useState('')
    const [options, setOptions] = useState(['', ''])
    const [multiple, setMultiple] = useState(false)

    const history = useHistory()

    function createOption(event) {
        event.preventDefault()

        const newOptions = [...options]
        newOptions.push('')

        setOptions(newOptions)
    }

    function handleSubmition(event) {
        event.preventDefault()

        const newPoll = {
            question: question,
            options: options.filter(value => (value !== '')),
            allow_multiple: multiple
        }

        api.post('poll', newPoll)
            .then(response => {
                const { url } = response.data
                history.push(`vote/${url}`)
            })
            .catch(error => console.log(error))
    }

    return (
        <div className='pollFormContainer'>
            <form onSubmit={handleSubmition}>
                <label htmlFor='question'>Question: </label>
                <input
                    required
                    type='text'
                    id='question'
                    value={question}
                    onChange={event => setQuestion(event.target.value)}
                />
                {options.map((option, index) => (
                    <div className='optionContaier' key={index}>
                        <label htmlFor={`option${index}`}>{`${index + 1}. `}</label>
                        <input
                            type='text'
                            id={`option${index}`}
                            value={option}
                            onChange={event => {
                                const modified = [...options]
                                modified[index] = event.target.value

                                setOptions(modified)
                            }}
                        />
                    </div>
                ))}
                <input
                    type='checkbox'
                    id='allowMultiple'
                    checked={multiple}
                    onChange={event => setMultiple(event.target.checked)}
                />
                <label htmlFor='allowMultiple'>Allow multiple answers?</label>

                <div className='buttonsContainer'>
                    <button onClick={createOption}>+</button>
                    <button type='submit'>Submit</button>
                </div>
            </form>
        </div>
    )
}

export default CreatePoll
