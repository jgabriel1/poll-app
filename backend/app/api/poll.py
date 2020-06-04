from fastapi import APIRouter, Depends, HTTPException, Response
from pymongo.database import Database
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND
)

from ..crud import crud_polls
from ..database.setup import get_db
from ..models import Poll, PollFromRequest, PollUrlPayload

router = APIRouter()


@router.post(
    '/poll',
    status_code=HTTP_201_CREATED,
    response_model=PollUrlPayload
)
def create(poll: PollFromRequest, database: Database = Depends(get_db)):
    poll_url = crud_polls.create(database, poll)
    return {'url': str(poll_url)}


@router.get('/poll/{poll_url}', response_model=Poll)
def show(poll_url: str, database: Database = Depends(get_db)):
    poll = crud_polls.find_by_url(database, poll_url)

    if not poll:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND, detail="This poll does not exist."
        )

    return poll


@router.delete('/poll/{poll_url}', status_code=HTTP_204_NO_CONTENT)
def destroy(poll_url: str, database: Database = Depends(get_db)):
    crud_polls.delete(database, poll_url)
    return Response(status_code=HTTP_204_NO_CONTENT)
