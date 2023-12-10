
from sqlalchemy.ext.asyncio import (
    async_sessionmaker, create_async_engine, AsyncSession
)
from internal.service.psql.tag import TagRepo

class Repo:
    def __init__(self, session:AsyncSession):
        self.session = session
        self.tag = self.tagRepo()
    
    def tagRepo(self):
        return TagRepo(self.session)