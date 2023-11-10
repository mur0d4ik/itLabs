from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    name = State()
    age = State()
    course = State()
    phone_number = State()
