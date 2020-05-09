const submitVotes = document.querySelector('#submit-votes')

submitVotes.addEventListener('click', () => {
    const checkboxes = document.querySelectorAll('.option-vote')
    const results = {
        'ids': Array.from(checkboxes, checkbox => checkbox.id),
        'results': Array.from(checkboxes, checkbox => checkbox.checked)
    }

    const currentURL = window.location.href

    fetch(currentURL, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(results),
        redirect: 'follow'
    }).then(response => {
        if (response.ok) {
            window.location.href = currentURL.replace('vote', 'result')
        }
    }).catch(error => console.log(error))
})