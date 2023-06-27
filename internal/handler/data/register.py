from aiogram import Dispatcher
from aiogram import types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Text

import datetime
import logging

from internal.handler.handler import Handler
from internal.model.user import User
from internal.service.psql.user import UserRepo


class DataRegister(Handler):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session


    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        pass