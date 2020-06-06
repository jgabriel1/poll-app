from fastapi import APIRouter, Depends, Response, HTTPException
from pymongo import MongoClient
from starlette.status import (
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_406_NOT_ACCEPTABLE
)

from ..crud import crud_votes
from ..database.setup import get_client
from ..models.payload import Votes

router = APIRouter()


@router.post('/vote/{poll_url}', status_code=HTTP_204_NO_CONTENT)
def update(
        poll_url: str,
        votes: Votes,
        client: MongoClient = Depends(get_client)
):
    computed = crud_votes.compute(client, poll_url, votes.voted)

    if computed is None:
        raise HTTPException(
            HTTP_404_NOT_FOUND, detail='This poll does not exist.'
        )

    if not computed:
        raise HTTPException(
            HTTP_406_NOT_ACCEPTABLE, detail='Cannot vote for multiple options!'
        )

    return Response(status_code=HTTP_204_NO_CONTENT)
