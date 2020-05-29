from datetime import timedelta
from typing import List

from pydantic import BaseModel


class PollSchema(BaseModel):
    question: str
    options: List[str]
    allow_multiple: bool
    track_ip: bool
    duration: timedelta
