from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):
    inventory = State()
    combat = State()
    inventori = State()
    endcombat = State()