import React, { useState } from 'react'
import { useHistory } from 'react-router-dom'

import OptionInput from './components/OptionInput'

import api from '../../services/api'

import './styles.css'

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
                <div className='questionContainer'>
                    <label htmlFor='question'>Question: </label>
                    <input
                        required
                        className='form-control'
                        type='text'
                        id='question'
                        value={question}
                        onChange={event => setQuestion(event.target.value)}
                    />
                </div>
                <div className="allowMultipleContainer">
                    <input
                        type='checkbox'
                        id='allowMultiple'
                        checked={multiple}
                        onChange={event => setMultiple(event.target.checked)}
                    />
                    <label htmlFor='allowMultiple'>Allow multiple answers?</label>
                </div>
                {options.map((option, index) => (
                    <OptionInput
                        value={option}
                        index={index}
                        changeHandler={event => {
                            const modified = [...options]
                            modified[index] = event.target.value

                            setOptions(modified)
                        }}
                    />
                ))}
                <div className='buttonsContainer'>
                    <button className='btn btn-primary' onClick={createOption}>+</button>
                    <button className='btn btn-primary' type='submit'>Create</button>
                </div>
            </form>
        </div>
    )
}

export default CreatePoll
