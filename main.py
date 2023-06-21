#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command


from pkg.config import config
from pkg.database import connection

logger = logging.getLogger(__name__)

CONFIG_FILE = "./config.ini"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
logger.info("Starting bot")

cnf = config.load_config(CONFIG_FILE)
storage = MemoryStorage()

bot = Bot(token=cnf.tg_data.token, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

logger.info("creating pool")


logger.info("Starting polling")


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        ses = await bot.get_session()
        await ses.close()
    

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped")
