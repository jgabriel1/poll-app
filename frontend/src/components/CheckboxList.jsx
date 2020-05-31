import React, { useEffect, useState } from 'react'

import api from '../services/api'

function CheckboxList({ pollUrl }) {
    const [question, setQuestion] = useState('')
    const [options, setOptions] = useState([])
    const [votes, setVotes] = useState([])
    const [multiple, setMultiple] = useState(false)

    useEffect(() => {
        api.get(`poll/${pollUrl}`)
            .then(response => {
                const poll = response.data

                setQuestion(poll.question)
                setOptions(poll.options.map(option => option.text))
                setVotes(Array(poll.options.length).fill(false))
                setMultiple(poll.allow_multiple)
            })
            .catch(error => console.log(error))
    }, [pollUrl])


    console.log('executed outside') // Why does this get executed 8 times?


    return (
        <div className='checkboxListContainer'>

        </div>
    )
}

export default CheckboxList
