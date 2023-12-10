#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
import logging
from venv import logger

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher

from pkg.config import config
from pkg.database import sqlalchemy as alch
from internal.handler.user import register
from internal.handler.data import new_data
from internal.handler import base_command
from internal.service.psql.repo import Repo


CONFIG_FILE = "./config.ini"


# async def reg_middleware(dp, session) -> None:
    # dp.middleware.setup(LoggingMiddleware())
    # dp.middleware.setup(AuthMiddleware(session))


async def reg_handlers(dp, repo:Repo) -> None:
    com_start = base_command.BaseComRegister()
    com_start.regisetr_hendlers(dp)

    user_reg = register.UserRegister(repo)
    user_reg.regisetr_hendlers(dp)


    # last handler
    data = new_data.Add_new_data(repo)
    data.regisetr_hendlers(dp)




async def main() -> None:
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    logger.info("Starting bot")

    cnf = config.load_config(CONFIG_FILE)

    bot = Bot(token=cnf.tg_data.token, parse_mode="HTML")
    dp = Dispatcher(storage=MemoryStorage())

    # session = connection.get_connection(cnf)
    session = await alch.get_async_session(cnf.db.database_url).asend(None)
    repo = Repo(session=session)
    # await reg_middleware(dp, session)
    await reg_handlers(dp, repo)

    try:
        await dp.start_polling(bot)
    except Exception as e :
        print(f"You error:\n{e}")
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
