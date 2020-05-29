from fastapi import APIRouter, Depends
from pymongo.database import Database

from ..crud import crud_polls
from ..database.setup import get_db
from ..models import Poll

router = APIRouter()


@router.post('/poll', status_code=201)
def new_poll(poll: Poll, database: Database = Depends(get_db)):
    poll_url = crud_polls.create(database, poll)
    return {'id': str(poll_url)}


@router.get('/poll/{poll_url}', response_model=Poll)
def fetch_poll(poll_url: str):
    pass


@router.delete('/poll/{poll_url}', status_code=204)
def delete_poll(poll_url: str):
    pass
