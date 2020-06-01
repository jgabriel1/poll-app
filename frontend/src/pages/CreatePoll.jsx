import React from 'react'

function CreatePoll() {

    function handleSubmition() { }

    return (
        <div className='pollFormContainer'>
            <form action={event => handleSubmition(event)}>
                <input type='text' name='question' id='question' />
            </form>
        </div>
    )
}

export default CreatePoll
