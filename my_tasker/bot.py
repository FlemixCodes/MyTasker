import coloredlogs
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.mongo import MongoStorage
from aiogram.loggers import dispatcher, event, middlewares, scene, webhook

from my_tasker.config import bot_config
from my_tasker.database import client
from my_tasker.handlers import routers_list


async def start_bot():
    """Запустить бота"""
    log_fmt = "%(asctime)s | %(levelname)s %(name)s | - %(message)s"
    coloredlogs.install(level="DEBUG", logger=dispatcher, fmt=log_fmt)
    coloredlogs.install(level="DEBUG", logger=event, fmt=log_fmt)
    coloredlogs.install(level="DEBUG", logger=middlewares, fmt=log_fmt)
    coloredlogs.install(level="DEBUG", logger=scene, fmt=log_fmt)
    coloredlogs.install(level="DEBUG", logger=webhook, fmt=log_fmt)

    bot = Bot(
        token=bot_config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode="HTML"),
    )

    dp = Dispatcher(storage=MongoStorage(client=client))
    dp.include_routers(*routers_list)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
