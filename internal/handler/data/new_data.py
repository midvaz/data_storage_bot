from aiogram import Dispatcher
from aiogram import types, F
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import datetime

from internal.handler.handler import Handler
from internal.service.psql.tag import TagRepo
from internal.service.psql.data import MessageHubRepo
from internal.models.tag import Tag
from internal.models.data import Message_hub
from internal.app import keyboard
from internal.service.psql.repo import Repo


class Data_states(StatesGroup):
    add_records = State()
    start_create_tag = State()


class Add_new_data(Handler):
    def __init__(self, repo:Repo) -> None:
        super().__init__()
        self.repo = repo


    async def __add_record(self, m: Message, state: FSMContext):
        await state.set_state(Data_states.add_records)
        data = await state.get_data()
        q='Вы можете отправить еще какиое-то сообщение или перейти дальше'
        batton_mass = []
        
        if data != {}:
            data = data['add_records']
            key = await keyboard.base_button(
            message_text='Далее',
            cbq='add_tag'
            )
            batton_mass.append(key)
        else:
            data = []
            
        if not(m.text is None) and m.text != '⬆️ Добавить запись':
            data.append(m.text)
            await state.update_data(add_records=data)
            key = await keyboard.base_button(
            message_text='Далее',
            cbq='add_tag'
            )
            batton_mass.append(key)
        else:
            q = 'Пока работаем только с тестом. Пришлите текст/ссылку'
            
        await m.answer(
            text=q,
            reply_markup=InlineKeyboardMarkup(inline_keyboard=batton_mass))
    
    
    async def __add_menu_tag(self, cbq:CallbackQuery, state: FSMContext):
        data = await state.get_data()
        if data == {}:
            await cbq.message.answer(
                text="Необходимо ввести сначала ввести текст/ссылку"
            )
            return
        q = 'Вы можете создать новый тег'
        tags = await self.repo.tag.read_by_tg_id(telegram_id=cbq.from_user.id)
        if not(tags is None):
            # если записей нет
            ...
            await state.clear()
            q= +"\nИли выбрать из уже существующего"
        # добавляет кноку новый тег
        batton_mass = []
        key = await keyboard.base_button(
            message_text='Новый тег',
            cbq='new_tag'
        )
        batton_mass.append(key)
        await cbq.message.bot.edit_message_text(
                text=q,
                chat_id=cbq.message.chat.id, 
                message_id=cbq.message.message_id,
                reply_markup=InlineKeyboardMarkup(inline_keyboard=batton_mass))
        
        
    async def add_new_tag(self, cbq:CallbackQuery, state: FSMContext):
        await state.set_state(Data_states.start_create_tag)
        q = 'Напиши имя тега'
        await cbq.message.bot.edit_message_text(
                text=q,
                chat_id=cbq.message.chat.id, 
                message_id=cbq.message.message_id,
                reply_markup=InlineKeyboardMarkup(inline_keyboard=[]))
    
    
    async def get_name_tag(self, m:Message, state: FSMContext):
        if m.text in None:
            await m.answer(text='Для имени тега подходит только текст')
        else:
            _ = await self.repo.tag.creat_tag(Tag(
                user_id=m.from_user.id,
                name=m.text,
                date_created = datetime.datetime.now(),
                date_updated = datetime.datetime.now(),
                data_deleted = None
            ))
            state.clear()
            m.answer(text='Тег создан')
            await self.__add_menu_tag()
        
        

# TODO: РАБОТА С ТЕГОМ
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
        # dp.message.register(self.__work_with_tags, Data_states.choice_tags)
        dp.callback_query.register(self.__add_menu_tag, F.data =='add_tag')
        
        dp.message.register(self.__add_record, F.text == '⬆️ Добавить запись')
        dp.message.register(self.__add_record, Data_states.add_records)
        dp.callback_query.register(self.add_new_tag, F.data=='new_tag')
        
        # dp.message.register(self.__create_new_tag, Data_states.start_create_tag)

        