from fastapi import APIRouter, Depends, Response, HTTPException
from pymongo.database import Database
from starlette.status import HTTP_204_NO_CONTENT, HTTP_406_NOT_ACCEPTABLE

from ..crud import crud_polls
from ..database.setup import get_db
from ..models import Votes

router = APIRouter()


@router.post('/vote/{poll_url}', status_code=HTTP_204_NO_CONTENT)
def compute_votes(
        poll_url: str, votes: Votes, database: Database = Depends(get_db)):
    updated: bool = crud_polls.compute_votes(database, poll_url, votes.voted)

    if not updated:
        raise HTTPException(
            HTTP_406_NOT_ACCEPTABLE, detail='Cannot vote for multiple options!'
        )

    return Response(status_code=HTTP_204_NO_CONTENT)
