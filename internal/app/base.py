from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import aiogram.utils.markdown as fmt

ABOUT = "🗃 О сервисе"
CANCEL_BUTTON = "◀️ отмена"
PROFILE = "📰 Профиль"

PRIVATE_INTERNAL_COMMANDS = [
    ABOUT,
    PROFILE,
]

PRIVATE_COMMANDS = [
]

help_message = f'''
📜 Тут вы можете сохранить и получить свои ссылки.


{ABOUT}
└ Узнать о сервисе

{PROFILE}
└ Узнать свои метрики

🗳 Доступные комманды
├ /help - инструкция
├ /menu - вызвать основное меню приложения
└ /reqister - регистрация
'''


about_service = fmt.text(
    fmt.text(
        fmt.hbold("📜 Я могу сохранять и предоставлять ваши ссылки и прочие материалы, которые вы мне скинете"),
    ),
    fmt.text(
        fmt.text("------------------------------------"),
        fmt.hitalic("Тут вы можете получить удобный доступ ко всем отправленным мне материалам.Поиск осуществляется по тегам или по описанию."),
        fmt.text("Поиск может осуществлять по тегам, которые вы предоставляете вместе с ссылкой."),
        fmt.text("Поиск может происходить и по тексту описания."),
        sep="\n\n"
    ),
    fmt.text(
        fmt.text("------------------------------------"),
        fmt.hbold("Инструкция доступна по команде /help"),
        sep="\n"
    ),
    sep="\n\n"
)


def default_menu():
    base_markup = ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    base_markup.add(*get_buttons_from_text_list(PRIVATE_INTERNAL_COMMANDS))
    return base_markup


def get_buttons_from_text_list(commands: list):
    ret = list()
    for item in commands:
        ret.append(KeyboardButton(item))

    return ret
