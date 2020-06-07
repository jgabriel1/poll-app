from secrets import token_urlsafe
from typing import Optional

from pymongo.client_session import ClientSession
from pymongo.database import Collection

from ..database.collections import get_polls_collection
from ..models.poll import PollFromRequest, PollInDB


def create(poll: PollFromRequest, session: ClientSession) -> str:
    url: str = token_urlsafe(nbytes=8)
    new_poll = PollInDB.serialize_from_request(poll, url)

    polls: Collection = get_polls_collection(session)

    polls.insert_one(new_poll.dict(), session=session)
    return new_poll.url


def find_by_url(poll_url: str, session: ClientSession) -> Optional[PollInDB]:
    polls: Collection = get_polls_collection(session)

    poll = polls.find_one({'url': poll_url}, session=session)

    if poll is not None:
        return PollInDB.parse_obj(poll)


def delete(poll_url: str, session: ClientSession) -> None:
    polls: Collection = get_polls_collection(session)

    polls.find_one_and_delete({'url': poll_url}, session=session)
