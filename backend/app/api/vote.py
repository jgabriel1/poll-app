from fastapi import APIRouter, Depends, HTTPException, Response
from pymongo.client_session import ClientSession
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_406_NOT_ACCEPTABLE
)

from ..crud import crud_polls, crud_votes
from ..database.connection import get_db
from ..models.payload import Votes

router = APIRouter()


@router.post('/vote/{poll_url}', status_code=HTTP_204_NO_CONTENT)
def update(
        poll_url: str,
        votes: Votes,
        session: ClientSession = Depends(get_db)
):
    with session.start_transaction():
        poll = crud_polls.find_by_url(poll_url, session)

        if poll is None:
            raise HTTPException(
                HTTP_404_NOT_FOUND,
                detail='This poll does not exist.'
            )

        multiple_voted: bool = sum(votes.voted) > 1
        if multiple_voted and not poll.allow_multiple:
            raise HTTPException(
                HTTP_406_NOT_ACCEPTABLE,
                detail='Cannot vote for multiple options!'
            )

        crud_votes.compute(poll, votes.voted, session)

    return Response(status_code=HTTP_204_NO_CONTENT)
