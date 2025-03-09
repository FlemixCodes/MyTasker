from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

button_1 = InlineKeyboardButton(text="Добавить задачу", callback_data="add_task")
button_2 = InlineKeyboardButton(text="Список задач", callback_data="get_tasks")
button_3 = InlineKeyboardButton(text="Удалить задачу", callback_data="delete_task")
button_4 = InlineKeyboardButton(text="Получить задачу", callback_data="get_task")

menu_keyboard = InlineKeyboardBuilder()
menu_keyboard.add(button_1, button_2, button_3)
