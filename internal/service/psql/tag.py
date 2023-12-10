import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
# import sqlalchemy


import logging

from internal.models.tag import Tag
from internal.models.user import User



class TagRepo:
    def __init__(self, session):
        self.session = session

    # TODO: ДОБАВИТЬ ПРОВЕРКУ НА ТАКОЕ СУЩЕСТВОВАНИЕ
    async def creat_tag(self, tag:Tag) -> Tag:
        try:
            returing_data = Tag(
                user_id= tag.user_id,
                name = tag.name,
                date_created = tag.date_created,
                date_updated = tag.date_updated,
                data_deleted = None
            )
            await self.session.add(returing_data)
            await self.session.commit()
            print("++++++++++++++++++++++++++++++++++++++++++++++я тут ау")

        except Exception as e:
            print(f"-----------------{e}")
            await self.session.rollback()

        return returing_data


    async def read_by_tg_id(self, telegram_id: int) -> Tag:
        user = await self.session.scalar(
            select(Tag).where(Tag.user_tg_id == telegram_id)
        )
        return user