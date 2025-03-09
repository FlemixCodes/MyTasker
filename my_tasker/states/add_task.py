from aiogram.fsm.state import State, StatesGroup


class AddTaskState(StatesGroup):
    name = State()
    description = State()
    deadline = State()
