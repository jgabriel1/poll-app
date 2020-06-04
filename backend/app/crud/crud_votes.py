from typing import List

from pymongo.database import Collection, Database
from pymongo.results import UpdateResult


def compute(db: Database, poll_url: str, votes: List[bool]) -> bool:
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
