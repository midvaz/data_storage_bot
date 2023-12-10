
from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



# inline_kb = InlineKeyboardMarkup().add(
#     InlineKeyboardButton(
#         'Использовать существующий', callback_data='attach_to_tag'),
#     InlineKeyboardButton(
#         'Создать новый', callback_data='create_new_tag')
# )

async def pay_basket(
    price:float,
    cb:str
):
    """
    Button for pay
    """
    button = [
        types.InlineKeyboardButton(text=f'Заказать за {price}руб.',
                                      callback_data=cb,
        )
    ]
    return button


inline_kb = InlineKeyboardBuilder()
inline_kb.add(InlineKeyboardButton(
        text="Использовать существующий",
        callback_data="attach_to_tag")
    )
inline_kb.add(InlineKeyboardButton(
        text="Создать новый",
        callback_data="create_new_tag")
    )

async def base_button(
    message_text:str,
    cbq
):
    """
    """
    return [
        types.InlineKeyboardButton(
            text=message_text,
            callback_data=cbq
        )
    ]
