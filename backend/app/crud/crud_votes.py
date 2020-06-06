from typing import List, Optional

from pymongo import MongoClient
from pymongo.database import Collection, Database
from pymongo.results import UpdateResult

from ..models.poll import PollInDB


def compute(
        client: MongoClient, poll_url: str, votes: List[bool]
) -> Optional[bool]:

    with client.start_session() as session:
        polls: Collection = client.poll_app.polls

        with session.start_transaction():
            poll = polls.find_one({'url': poll_url}, session=session)

            if poll is None:
                return None

            poll = PollInDB.parse_obj(poll)

            multiple_voted: bool = sum(votes) > 1
            if multiple_voted and not poll.allow_multiple:
                return False

            polls.update_one(
                filter={'url': poll.url},
                update={
                    '$inc': {
                        f'options.{index}.votes': 1
                        for index, voted in enumerate(votes) if voted
                    }
                },
                session=session
            )

            return True


def compute_old(db: Database, poll_url: str, votes: List[bool]) -> bool:
    '''
    This operation is deprecated.
    '''
    raise DeprecationWarning

    update_votes: dict = {
        f'options.{index}.votes': 1
        for index, voted in enumerate(votes) if voted
    }

    multiple_voted: bool = sum(votes) > 1

    # Check if it allows multiple votes only when recieving multiple votes:
    filters: dict = {'url': poll_url}
    if multiple_voted:
        filters.update({'allow_multiple': True})

    polls: Collection = db.polls
    result: UpdateResult = polls.update_one(filters, {'$inc': update_votes})

    return result.modified_count > 0
