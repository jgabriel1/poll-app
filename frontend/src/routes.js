import React from 'react'

import { BrowserRouter, Route, Switch } from 'react-router-dom'

import CreatePoll from './pages/CreatePoll'
import VotePoll from './pages/VotePoll'
import Results from './pages/Results'

function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path='/' component={CreatePoll} />
                <Route path='/vote/:pollUrl' component={VotePoll} />
                <Route exact path='/results/:pollUrl' component={Results} />
            </Switch>
        </BrowserRouter>
    )
}

export default Routes
