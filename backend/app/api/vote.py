from fastapi import APIRouter, Depends, Response
from pymongo.database import Database
from starlette.status import HTTP_204_NO_CONTENT

from ..crud import crud_polls
from ..database.setup import get_db
from ..models import Votes

router = APIRouter()


@router.post('/vote/{poll_url}', status_code=HTTP_204_NO_CONTENT)
def compute_votes(
        poll_url: str, votes: Votes, database: Database = Depends(get_db)):
    crud_polls.compute_votes(database, poll_url, votes.voted)
    return Response(status_code=HTTP_204_NO_CONTENT)
