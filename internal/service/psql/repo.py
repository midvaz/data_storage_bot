
from sqlalchemy.ext.asyncio import (
    async_sessionmaker, create_async_engine, AsyncSession
)

class Repo:
    def __init__(self, session:AsyncSession):
        self.session = session