from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from my_tasker.database import client
from my_tasker.utils.lang import get_string

router = Router(name="tasks")


@router.message(Command("tasks"))
@router.message(F.data == "get_tasks")
async def get_tasks(message: Message):
    await message.answer(get_string("get_tasks_text"))


@router.message(Command("task"))
@router.message(F.data == "get_task")
async def get_task(message: Message):
    await message.answer(get_string("get_task_text"))


@router.message(Command("add_task"))
@router.message(F.data == "add_task")
async def add_task(message: Message):
    await message.answer(get_string("get_task_add_text"))


@router.message(Command("delete_task"))
@router.message(F.data == "delete_task")
async def delete_task(message: Message):
    await message.answer(get_string("get_task_delete_text"))
