
from aiogram.fsm.state import State, StatesGroup

class Data_states(StatesGroup):
    choice_tags = State()
    start_create_tag = State()