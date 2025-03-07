from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from my_tasker.config import Emoji, bot_config

router = Router(name="basic")

@router.message(CommandStart())
async def start_handler(message: Message):
    out_text = "Приветствую! Я бот который поможет тебе с планировкой задач и напомнит об их выполнении!"
    await message.answer(out_text)

@router.message(Command("ping"))
async def ping_handler(message: Message):
    latency = round(datetime.now().timestamp() - message.date.timestamp(), 2) * 1000
    await message.answer(f"{Emoji.SETTINGS} Бот ответил за: <b>{latency}</b>мс.")

@router.message(Command("privacy"))
async def privacy_handler(message: Message):
    await message.answer(f"{bot_config.privacy.get_secret_value()}")