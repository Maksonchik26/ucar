from datetime import datetime

from pydantic import BaseModel

from common.enums import SentimentEnum


class ReviewIn(BaseModel):
    text: str


class ReviewOut(ReviewIn):
    id: int
    sentiment: SentimentEnum
    created_at: datetime
