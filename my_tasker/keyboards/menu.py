from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_keyboard = InlineKeyboardBuilder()
menu_keyboard.add(
    InlineKeyboardButton(text="Добавить задачу", callback_data="add_task")
)
menu_keyboard.add(
    InlineKeyboardButton(text="Получить задачу", callback_data="get_task")
)
menu_keyboard.add(
    InlineKeyboardButton(text="Удалить задачу", callback_data="delete_task")
)
menu_keyboard.add(
    InlineKeyboardButton(text="Получить список задач", callback_data="get_tasks")
)
