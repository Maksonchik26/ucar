from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Text

from db.base import Base


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    sentiment: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(Text)
