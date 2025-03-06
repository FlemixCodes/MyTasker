from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from my_tasker.config import Emoji

router = Router(name="basic")


@router.message(CommandStart())
async def start_handler(message: Message):
    out_text = "Приветствую! Я бот который напомнит тебе о задачах!"
    await message.answer(out_text)


@router.message(Command("ping"))
async def ping_handler(message: Message):
    latency = round(datetime.now().timestamp() - message.date.timestamp(), 2) * 1000
    await message.answer(f"{Emoji.SETTINGS} Бот ответил за: <b>{latency}</b>мс.")
