from secrets import token_urlsafe
from typing import List

from pymongo.database import Collection, Database

from ..models import Poll, PollInDB


def create(database: Database, poll: Poll) -> str:
    new_poll = PollInDB.parse_obj(poll)
    new_poll.url = token_urlsafe(nbytes=8)

    polls: Collection = database.polls
    polls.insert_one(new_poll.dict())
    return new_poll.url


def find_by_url(database: Database, poll_url: str) -> dict:
    polls: Collection = database.polls
    poll = polls.find_one({'url': poll_url})
    return poll


def delete(database: Database, poll_url: str) -> None:
    polls: Collection = database.polls
    polls.delete_one({'url': poll_url})


def compute_votes(
        database: Database, poll_url: str, votes: List[bool]) -> None:
    update_votes = {
        f'options.{i}.votes': 1
        for i, vote in enumerate(votes) if vote
    }
    polls: Collection = database.polls
    polls.update_one({'url': poll_url}, {'$inc': update_votes})
