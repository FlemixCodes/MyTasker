from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

menu_keyboard = InlineKeyboardBuilder()
menu_keyboard.add(InlineKeyboardButton("Добавить задачу", callback_data="add_task"))
menu_keyboard.add(InlineKeyboardButton("Получить задачу", callback_data="get_task"))
menu_keyboard.add(InlineKeyboardButton("Удалить задачу", callback_data="delete_task"))
menu_keyboard.add(
    InlineKeyboardButton("Получить список задач", callback_data="get_tasks")
)
