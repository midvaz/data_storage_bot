


from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped
from sqlalchemy.ext.asyncio import (
    async_sessionmaker, create_async_engine, AsyncSession
)

from pkg.config import config

# DATABASE_DRAVER = "postgresql+asyncpg://"




async def get_async_session(url_db:str) -> AsyncSession:
    engine = create_async_engine(
    url=url_db,
    echo=True
    )

    async_session = async_sessionmaker(
        bind=engine,
        expire_on_commit=False
    )

    async with async_session() as session:
        try:  
            yield session
        except Exception:
            await session.rollback()
        finally:
            await session.close()

# AsyncDbSession = Annotated[AsyncSession, Depends(get_async_session)]