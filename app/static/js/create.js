const submitButton = document.querySelector('#submit-poll-form')

submitButton.addEventListener('click', () => {
    const question = document.querySelector('#poll-question')
    const allowMultiple = document.querySelector('#allow-multiple')
    const options = Array.from(
        document.querySelectorAll('.poll-option'),
        option => option.value
    )

    const data = {
        'question': question.value,
        'allow_multiple': allowMultiple.checked,
        'options': options
    }

    fetch('/create', {
        method: 'POST',
        redirect: 'follow',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    }).then(response => {
        if (response.redirected) {
            window.location.href = response.url
        }
    })
})
