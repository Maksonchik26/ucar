import datetime

from sqlalchemy import select

from crud.common import CRUD
from db.models import Review
from common.enums import SentimentEnum
from services.reviews import detect_sentiment
from schemas.reviews import ReviewIn


class ReviewsCRUD(CRUD):
    async def read_all (self, sentiment: SentimentEnum, limit: int = 10, offset: int = 0):
        reviews = await self.session.execute(select(Review).limit(limit).offset(offset).where(Review.sentiment == sentiment.value))
        result = reviews.scalars().all()

        return result

    async def create(self, review_data: ReviewIn):
        sentiment = detect_sentiment(review_data.text)
        review = Review(sentiment=sentiment.value,
                             text=review_data.text,
                             created_at=datetime.datetime.now().isoformat())

        self.session.add(review)
        await self.session.commit()
        await self.session.refresh(review)

        return review
