"""This file represent startup bot logic."""
import asyncio
import logging

from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage

from src.configuration import conf
from src.bot.dispatcher import get_dispatcher


async def start_bot():
    """This function will start bot with polling mode."""
    bot = Bot(token=conf.bot.token)
    dp = get_dispatcher(storage=MemoryStorage())

    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types()
    )


if __name__ == '__main__':
    logging.basicConfig(level=conf.logging_level)
    asyncio.run(start_bot())
