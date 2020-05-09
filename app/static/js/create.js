const moreButton = document.querySelector('#add-option')
const submitButton = document.querySelector('#submit-poll-form')

moreButton.addEventListener('click', () => {
    const optionList = document.querySelector('#option-list')
    const optionContainer = optionList.querySelector('.option-container')
    const clone = optionContainer.cloneNode(true)

    const changeInChild = (attribute, count) => {
        let child = clone.querySelector('input')
        let value = child.getAttribute(attribute).replace('0', count)
        child.setAttribute(attribute, value)
    }

    changeInChild('id', optionList.childElementCount)
    changeInChild('name', optionList.childElementCount)

    optionList.appendChild(clone)
})

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
