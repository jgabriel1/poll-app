from secrets import token_urlsafe
from typing import Optional

from pymongo.database import Collection, Database

from ..models.poll import Poll, PollFromRequest, PollInDB


def create(db: Database, poll: PollFromRequest) -> str:
    url = token_urlsafe(nbytes=8)
    new_poll = PollInDB.serialize_from_request(poll, url)

    polls: Collection = db.polls
    polls.insert_one(new_poll.dict())
    return new_poll.url


def find_by_url(db: Database, poll_url: str) -> Optional[Poll]:
    polls: Collection = db.polls
    poll = polls.find_one({'url': poll_url})

    if poll is not None:
        return Poll.parse_obj(poll)


def delete(db: Database, poll_url: str) -> None:
    polls: Collection = db.polls
    polls.find_one_and_delete({'url': poll_url})
