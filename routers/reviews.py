from fastapi import APIRouter, Depends, status

from crud.reviews import ReviewsCRUD
from schemas.reviews import ReviewOut, ReviewIn
from common.enums import SentimentEnum


router = APIRouter(
    prefix='/reviews',
    tags=['reviews']
)


@router.get("/", response_model=list[ReviewOut], status_code=status.HTTP_200_OK)
async def get_reviews(sentiment: SentimentEnum,
                      reviews_crud: ReviewsCRUD = Depends(),
                      limit: int = 10,
                      offset: int = 0):
    reviews = await reviews_crud.read_all(sentiment, limit, offset)

    return reviews


@router.post("/", response_model=ReviewOut, status_code=status.HTTP_201_CREATED)
async def create_review(review_data: ReviewIn,
                        reviews_crud: ReviewsCRUD = Depends()):
    review = await reviews_crud.create(review_data)

    return review
