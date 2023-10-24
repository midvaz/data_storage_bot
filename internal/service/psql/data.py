import datetime
from typing import List

from sqlalchemy import select
# import sqlalchemy


import logging

from internal.models.data import Message_hub
from internal.service.psql.repo import Repo


class MessageHubRepo(Repo):
    def __init__(self, session):
        Repo.__init__(self, session)


    async def creat_data(self, message_hub:Message_hub) -> None:
        try:
            self.session.add(message_hub)
            await self.session.commit()

        except Exception as e:
            print(f"-----------------{e}")
            self.session.rollback()


    # async def read_user_by_tg_id(self, telegram_id: int) -> Message_hub:
    #     user = await self.session.scalar(
    #         select(Message_hub).where(Message_hub.telegram_id == telegram_id)
    #     )
    #     return user