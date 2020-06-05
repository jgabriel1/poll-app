from typing import List

from pydantic import BaseModel

from .option import Option


class Poll(BaseModel):
    question: str
    options: List[Option]
    allow_multiple: bool


class PollFromRequest(Poll):
    options: List[str]


class PollInDB(Poll):
    url: str

    @classmethod
    def serialize_from_request(cls, poll: PollFromRequest, url: str):
        options = [
            {
                'text': option,
                'votes': 0
            }
            for option in poll.options
        ]

        serialized = cls(
            url=url,
            options=options,
            **poll.dict(exclude={'options'})
        )

        return serialized
