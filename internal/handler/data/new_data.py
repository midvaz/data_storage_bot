from aiogram import Dispatcher
from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

import datetime

from internal.handler.handler import Handler
from internal.app import keyboard
# from internal.app import state
from internal.service.psql.tag import TagRepo
from internal.service.psql.data import MessageHubRepo
from internal.models.tag import Tag
from internal.models.data import Message_hub
from pkg.utils.scripts import Utils


class Data_states(StatesGroup):
    choice_tags = State()
    start_create_tag = State()


class Add_new_data(Handler):
    def __init__(self, session) -> None:
        super().__init__()
        self.session = session


    async def __add_record(self, m: Message, state) -> None:
        message_data = Utils.get_tg_file_id_name_type(m)
        await state.set_state(Data_states.choice_tags.state)
        await state.update_data(user_message=message_data)
        # возможно прям тут нужно сделать занесение в базу


    async def __work_with_tags(self, m: Message, state: FSMContext) -> None:
        await m.reply("Какой тег присвоить", reply_markup=keyboard.inline_kb)
        print(await state.get_data())

    
    async def __start_new_tag(self, m: Message, state: FSMContext) -> None:
        # await m.answer("Введите название нового тега")
        await m.bot.send_message(chat_id=m.from_user.id,text="Введите название нового тега")
        await state.set_state(Data_states.start_create_tag)


    async def __create_new_tag(self, m: Message, state: FSMContext) -> None:
        new_tag = await TagRepo(self.session).creat_tag(
            tag=Tag(
                user_id= m.from_user.id,
                name = m.text,
                date_created = datetime.datetime.now(),
                date_updated = datetime.datetime.now(),
                data_deleted = None
            )
        )
        await MessageHubRepo(self.session).creat_data(
            message_hub= Message_hub(
                user_id=m.from_user.id,
                tag_id=new_tag.id,
                descrition = '',
                body_data = state.get_data("user_message"),
                date_created = datetime.datetime.now(),
                date_updated = datetime.datetime.now(),
                data_deleted = None
            )
        )
        await state.finish()
        await m.answer("Готов")


         

    def regisetr_hendlers(self, dp: Dispatcher) -> None:
        dp.register_message_handler(self.__work_with_tags, state=Data_states.choice_tags)
        dp.register_callback_query_handler(self.__start_new_tag, lambda callback: callback.data =='create_new_tag', state="*")
        dp.register_message_handler(self.__create_new_tag, state=Data_states.start_create_tag)
        #TODO: добавить хендлер с выбором
        

        dp.register_message_handler(self.__add_record, content_types=types.ContentTypes.ANY, state="*")
        