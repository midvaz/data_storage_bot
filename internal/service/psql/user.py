import datetime
from typing import List

from sqlalchemy import select
# import sqlalchemy


import logging

from internal.model.user import User
from internal.service.psql.repo import Repo


class UserRepo(Repo):
    def __init__(self, session):
        Repo.__init__(self, session)


    async def creat_user(self, user:User) -> None:
        try:
            # await self.session.add(user)
            self.session.add(user)
            await self.session.commit()

        except Exception as e:
            print(f"-----------------{e}")
            
            self.session.rollback()


    async def read_user_by_tg_id(self, telegram_id: int) -> User:
        user = await self.session.scalar(
            select(User).where(User.telegram_id == telegram_id)
        )
        return user
    

    # async def user_exist(self, telegram_id):
    #     exist = await self.session.scalar(
    