from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from my_tasker.config import bot_config
from my_tasker.handlers import routers_list


async def start_bot():
    """Запустить бота"""
    bot = Bot(
        token=bot_config.bot_token.get_secret_value(),
        default=DefaultBotProperties(parse_mode="HTML"),
    )

    dp = Dispatcher()
    dp.include_routers(*routers_list)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
