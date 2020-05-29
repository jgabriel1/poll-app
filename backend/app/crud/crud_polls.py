from pymongo.database import Database

from ..models import Poll


def create(database: Database, poll: Poll) -> str:
    polls = database.polls
    return polls.insert_one(poll.dict()).inserted_id


def read(database: Database, poll_url: str) -> Poll:
    pass


def delete(database: Database, poll_url: str) -> None:
    pass


def compute_votes():
    pass
