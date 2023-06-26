

from aiogram import Dispatcher
from aiogram import types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Text

import datetime
import logging

from internal.handler.handler import Handler
from internal.model.user import User
from internal.service.psql.user import UserRepo


class UserRegister(Handler):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session
        
    async def register_user(self, m: types.Message) -> None:
        await UserRepo(self.session).creat_user(
            User(
                telegram_id= 0,
                is_admin = False,
                date_created = datetime.datetime.now(),
                date_updated = datetime.datetime.now(),
                data_deleted = None
            )
        )
        await m.reply(f"Регистарация прошла успешно {m.from_user.id}",  reply=False)


    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.register_user, commands=['register'])