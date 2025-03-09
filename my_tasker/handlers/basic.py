from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from my_tasker.config import Emoji, bot_config
from my_tasker.keyboards.menu import menu_keyboard
from my_tasker.utils.lang import get_string

router = Router(name="basic")


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(get_string("get_start_text"))


@router.message(Command("ping"))
async def ping_handler(message: Message):
    latency = round(datetime.now().timestamp() - message.date.timestamp(), 2) * 1000
    text = get_string("get_ping_text").format(emoji=Emoji.SETTINGS, latency=latency)
    await message.answer(text)


@router.message(Command("privacy"))
async def privacy_handler(message: Message):
    await message.answer(get_string("get_privacy_text"))


@router.message(Command("menu"))
async def menu_handler(message: Message):
    await message.answer(
        get_string("get_menu_text"), reply_markup=menu_keyboard.as_markup()
    )
