from secrets import token_urlsafe

from pymongo.database import Collection, Database

from ..models import Poll, PollInDB, PollCreation


def create(db: Database, poll: PollCreation) -> str:
    poll.options = [
        {'text': option, 'votes': 0} for option in poll.options
    ]

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
