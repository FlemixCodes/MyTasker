from datetime import datetime

from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from my_tasker.config import Emoji

router = Router(name="basic")

privacy = "Этот документ описывает политику конфиденциальности для бота 'MyTasker'. \nЕсли у вас есть вопросы, свяжитесь с нами @whynoet @deathrideeet\n\nСобираемая информация\nМы собираем следующие данные:\n- Личные данные указанные в профиле, такие как имя, фамилия, username, ID (IDentificator) пользователя*\n- Сообщения, отправленные боту в личных сообщениях*\n- Команды, отправленные боту в личных сообщениях*\n* - наш бот не работает ни с чем кроме личных сообщений, данный функционал не умеет работать с чатами и так далее.\n\nИспользование данных\nСобранные данные используются для:\n- Обработки запросов пользователей\n- Исправления ошибок связанных с командами\n- Улучшения работы бота\n- Анализа использования сервиса\n\nХранение данных\nДанные хранятся на сервере без срока хранения.\nНекоторые данные могут удаляться по мере необходимости.\n\nПередача данных третьим лицам\nМы не передаем ваши данные третьим лицам без вашего согласия, за исключением случаев, предусмотренных законом.\n\nИзменения в политике конфиденциальности\nМы оставляем за собой право обновлять эту политику. Обо всех изменениях мы уведомим вас через наш бот или канал в телеграме (https://t.me/+9m0F4Kkww4Y0YTg6)\n\nКонтактная информация\nЕсли у вас есть вопросы, свяжитесь с нами @whynoet @deathrideeet."

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
    await message.answer(f"{privacy}")
