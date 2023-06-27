import logging
import types

from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text


from internal.handler.handler import Handler
from internal.app.base import default_menu, help_message, about_service, ABOUT, PROFILE


logger = logging.getLogger(__name__)
reg_c_data = CallbackData("register")


class BaseComRegister(Handler):
    @staticmethod
    async def start(m: Message) -> None:
        await m.reply(
            about_service,
            reply=False,
            reply_markup=BaseComRegister.start_registration_keyboard()
        )

    @staticmethod
    def start_registration_keyboard() -> None:
        return InlineKeyboardMarkup(row_width=1).add(
            InlineKeyboardButton(
                text="Начать регистрацию",
                callback_data=reg_c_data.new(),
            )
        )
    
    @staticmethod
    async def cmd_menu(m: Message):
        await m.reply("Меню обновлено", reply_markup=default_menu(), reply=False)

    @staticmethod
    async def cmd_help(m: Message):
        await m.reply(help_message, reply_markup=default_menu(), reply=False)

    @staticmethod
    async def cmd_about(m: Message):
        await m.reply(about_service, reply_markup=default_menu(), reply=False)


    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.start, commands=["start"])
        dp.register_message_handler(self.cmd_menu, commands=['menu'])
        dp.register_message_handler(self.cmd_help, commands=['help'])

        dp.register_message_handler(self.cmd_about, commands=['about'])
        dp.register_message_handler(self.cmd_about, Text(equals=ABOUT))

