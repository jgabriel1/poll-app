from secrets import token_urlsafe
from typing import List

from pymongo.database import Collection, Database
from pymongo.results import UpdateResult

from ..models import Poll, PollInDB


def create(db: Database, poll: Poll) -> str:
    new_poll = PollInDB.parse_obj(poll)
    new_poll.url = token_urlsafe(nbytes=8)

    polls: Collection = db.polls
    polls.insert_one(new_poll.dict())
    return new_poll.url


def find_by_url(db: Database, poll_url: str) -> Poll:
    polls: Collection = db.polls
    poll = polls.find_one({'url': poll_url})
    return Poll.parse_obj(poll)


def delete(db: Database, poll_url: str) -> None:
    polls: Collection = db.polls
    polls.delete_one({'url': poll_url})


def compute_votes(
        db: Database, poll_url: str, votes: List[bool]) -> bool:

    update_votes: dict = {
        f'options.{index}.votes': 1
        for index, voted in enumerate(votes) if voted
    }

    multiple_voted: bool = sum(votes) > 1

    # Check if it allows multiple votes only when recieving multiple votes:
    filters: dict = {
        'url': poll_url, 'allow_multiple': True
    } if multiple_voted else {
        'url': poll_url
    }

    polls: Collection = db.polls
    result: UpdateResult = polls.update_one(filters, {'$inc': update_votes})

    return result.modified_count > 0
