from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config.settings import get_settings


settings = get_settings()


engine = create_async_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)


AsyncSessionFactory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


from collections.abc import AsyncGenerator


async def get_session() -> AsyncGenerator[AsyncSession, None]:

    async with AsyncSessionFactory() as session:

        yield session