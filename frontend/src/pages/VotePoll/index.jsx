import React, { useState, useEffect } from 'react'
import { useHistory } from 'react-router-dom'

import Checkbox from './components/Checkbox'

import api from '../../services/api'

import './styles.css'

function VotePoll(props) {
    const { pollUrl } = props.match.params

    const [question, setQuestion] = useState('')
    const [options, setOptions] = useState([])
    const [multiple, setMultiple] = useState(false)

    const history = useHistory()

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
            .then(() => {
                history.push(`/results/${pollUrl}`)
            })
            .catch(error => console.log(error))
    }

    return (
        <div className='votePollContainer'>
            <legend>{question}</legend>
            <div className='optionsContainer'>
                {options.map(
                    (option, i) => (
                        <Checkbox
                            key={i}
                            index={i}
                            voteHandler={handleCheck}
                            {...option}
                        />
                    )
                )}
            </div>
            <div className="buttonContainer">
                <button className='btn btn-primary' onClick={handleSubmition}>Submit</button>
            </div>
        </div>
    )
}

export default VotePoll
