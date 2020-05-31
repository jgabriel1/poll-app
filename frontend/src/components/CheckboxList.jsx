import React, { useState, useEffect } from 'react'

import Checkbox from './Checkbox'

import api from '../services/api'

function CheckboxList({ pollUrl }) {
    const [question, setQuestion] = useState('')
    const [options, setOptions] = useState([])
    const [multiple, setMultiple] = useState(false)

    useEffect(() => {
        api.get(`poll/${pollUrl}`)
            .then(response => {
                const poll = response.data

                setQuestion(poll.question)
                setOptions(poll.options.map(
                    option => ({ optionText: option.text, isVoted: false })
                ))
                setMultiple(poll.allow_multiple)
            })
            .catch(error => console.log(error))
    }, [pollUrl])

    function handleCheck(event, index) {
        let updatedOptions = [...options]
        let clickedOption = updatedOptions[index]

        // Reset all options if user is not allowed to vote for multiple:
        if (!multiple) {
            updatedOptions.forEach(option => { option.isVoted = false })
        }

        clickedOption.isVoted = event.target.checked

        setOptions(updatedOptions)
    }

    function handleSubmition() {
        const body = {
            voted: options.map(option => option.isVoted)
        }

        api.post(`vote/${pollUrl}`, body)
            .then(response => console.log(response))
            .catch(error => console.log(error))
    }

    return (
        <div className='checkboxListContainer'>
            <legend>{question}</legend>
            {options.map((option, i) => (
                <Checkbox index={i} voteHandler={handleCheck} {...option} />
            ))}
            <button onClick={handleSubmition}>Submit</button>
        </div>
    )
}

export default CheckboxList
