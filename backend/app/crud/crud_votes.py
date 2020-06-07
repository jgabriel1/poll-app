from typing import List

from pymongo.client_session import ClientSession
from pymongo.database import Collection

from ..database.collections import get_polls_collection
from ..models.poll import PollInDB


def compute(poll: PollInDB, votes: List[bool], session: ClientSession) -> None:
    polls: Collection = get_polls_collection(session)

    # Increase by 1 the votes on each index voted:
    update_query = {
        '$inc': {
            f'options.{index}.votes': 1
            for index, voted in enumerate(votes) if voted
        }
    }

    polls.update_one(
        filter={'url': poll.url}, update=update_query, session=session
    )
