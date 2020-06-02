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
            <table className='optionsList table table-striped'>
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col"></th>
                        <th scope="col">Votes</th>
                        <th scope="col">%</th>
                    </tr>
                </thead>
                <tbody>
                    {results.map((result, index) => {
                        let { text, votes } = result
                        let percent = 100 * (votes / total)

                        return (
                            <tr className='optionContainer' key={index}>
                                <th scope='row'>{index + 1}</th>
                                <td className='optionText'>{text}</td>
                                <td className='optionVotes'>{votes}</td>
                                <td className='optionPercent'>{`${percent.toFixed(2)}%`}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default Results
