import React, { useState, useEffect } from 'react'

import api from '../../services/api'

import './styles.css'

function Results(props) {
    const { pollUrl } = props.match.params

    const [question, setQuestion] = useState('')
    const [results, setResults] = useState([])

    useEffect(() => {
        api.get(`poll/${pollUrl}`)
            .then(result => {
                const { question, options } = result.data

                options.sort((a, b) => (b.votes - a.votes))
                setResults(options)

                setQuestion(question)
            })
            .catch(error => console.log(error))
    }, [pollUrl])

    const total = results.reduce((accumulator, result) => {
        let { votes } = result
        return (accumulator + votes)
    }, 0)

    return (
        <div className='resultsContainer'>
            <p className='pollQuestion'>{question}</p>
            <ul className='optionsList'>
                {results.map((result, index) => {
                    let { text, votes } = result
                    let percent = 100 * (votes / total)

                    return (
                        <li className='optionContainer' key={index}>
                            <div className='optionText'>{text}</div>
                            <div className='optionVotes'>{votes}</div>
                            <div className='optionPercent'>{`${percent.toFixed(2)}%`}</div>
                        </li>
                    )
                })}
            </ul>
        </div>
    )
}

export default Results
