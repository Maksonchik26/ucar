from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker


DATABASE_URL = "sqlite+aiosqlite:///reviews.db"


engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()

async_session = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    """
    Return a new database session to use in FastAPI dependency.

    Returns:
        Session: A new database session.

    """
    async with async_session() as session:
        yield session


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
