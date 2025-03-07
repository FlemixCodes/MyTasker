from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="tasks")


@router.message(Command("tasks"))
@router.message(F.data == "get_tasks")
async def get_tasks(message: Message): ...


@router.message(Command("task"))
@router.message(F.data == "get_task")
async def get_task(message: Message): ...


@router.message(Command("add_task"))
@router.message(F.data == "add_task")
async def add_task(message: Message): ...


@router.message(Command("delete_task"))
@router.message(F.data == "delete_task")
async def delete_task(message: Message): ...
