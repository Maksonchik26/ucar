from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.base import get_async_session


class CRUD:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
