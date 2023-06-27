#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
from venv import logger

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Command

from pkg.config import config
# from pkg.database import connection
from pkg.database import sqlalchemy as alch
from pkg.middlewares.auth import AuthMiddleware

from internal.handler.user import register


CONFIG_FILE = "./config.ini"


async def main():
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.info("Starting bot")

    cnf = config.load_config(CONFIG_FILE)
    storage = MemoryStorage()

    bot = Bot(token=cnf.tg_data.token, parse_mode="HTML")
    dp = Dispatcher(bot, storage=storage)

    # session = connection.get_connection(cnf)
    session = await alch.get_async_session(cnf.db.database_url).asend(None)
 
    dp.middleware.setup(AuthMiddleware(session))


    user_reg = register.UserRegister(session)
    user_reg.regisetr_hendlers(dp)

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
