import logging
import types

from aiogram import Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters.command import Command

from internal.handler.handler import Handler
from internal.app.base import default_menu, help_message, about_service, ABOUT, PROFILE


logger = logging.getLogger(__name__)
# TODO: ПОЧИНИТЬ КОЛБЕК 



class BaseComRegister(Handler):
    def __init__(self):
        pass


    @staticmethod
    async def __start(m: Message) -> None:
        await m.reply(
            about_service,
            reply=False,
            reply_markup=BaseComRegister.__start_registration_keyboard()
        )

    @staticmethod
    def __start_registration_keyboard() -> None:
        pass
    
    @staticmethod
    async def __cmd_menu(m: Message):
        await m.reply("Меню обновлено", reply_markup=default_menu(), reply=False)

    @staticmethod
    async def __cmd_help(m: Message):
        await m.reply(help_message, reply_markup=default_menu().as_markup(resize_keyboard=True), reply=False)

    @staticmethod
    async def __cmd_about(m: Message):
        await m.reply(about_service, reply_markup=default_menu(), reply=False)


    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        dp.message.register(self.__start, Command("start"))
        dp.message.register(self.__cmd_menu, Command("start"))
        dp.message.register(self.__cmd_help, Command("help"))

        dp.message.register(self.__cmd_about, Command("about"))
        dp.message.register(self.__cmd_about, F.text ==ABOUT)

