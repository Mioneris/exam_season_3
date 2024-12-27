import asyncio
import logging

from bot_config import bot, dp, database
from handlers.complaint import complaint_router
from handlers.start import start_router


async def on_startup():
    database.create_tables()


async def main():
    dp.include_routers(start_router,
                       complaint_router)

    dp.startup.register(on_startup)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
