import logging

import asyncpg
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware

from aiogram import types


from internal.service.psql.user import UserRepo


logger = logging.getLogger(__name__)


# class AuthMiddleware(LifetimeControllerMiddleware):
#     def __init__(self, session):
#         super().__init__()
#         self.session = session

#     async def pre_process(self, obj: types.Update, data, *args):
#         if isinstance(obj, types.Message):
#                 return

#         elif isinstance(obj, types.CallbackQuery):
#             if obj.data == "register":
#                 return

#             chat_id = obj.message.chat.id
#             reply_obj = obj.message
#         else:
#             return

#         authorized = await self.is_user_authorized(self.session, chat_id)
        
#         await self.session.close()
#         if not authorized:
#             await reply_obj.answer("Авторизуйтесь для использования бота. Команда /register")
#             raise CancelHandler()


#     @staticmethod
#     async def is_user_authorized(ses, telegram_id):
#         return await UserRepo(ses).read_user_by_tg_id(
#             telegram_id
#         )

# class AuthMiddleware(BaseMiddleware)
