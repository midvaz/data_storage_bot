
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



inline_kb = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        'Использовать существующий', callback_data='attach_to_tag'),
    InlineKeyboardButton(
        'Создать новый', callback_data='create_new_tag')
)
