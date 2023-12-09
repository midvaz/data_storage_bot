
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



# inline_kb = InlineKeyboardMarkup().add(
#     InlineKeyboardButton(
#         'Использовать существующий', callback_data='attach_to_tag'),
#     InlineKeyboardButton(
#         'Создать новый', callback_data='create_new_tag')
# )

inline_kb = InlineKeyboardBuilder()
inline_kb.add(InlineKeyboardButton(
        text="Использовать существующий",
        callback_data="attach_to_tag")
    )
inline_kb.add(InlineKeyboardButton(
        text="Создать новый",
        callback_data="create_new_tag")
    )
