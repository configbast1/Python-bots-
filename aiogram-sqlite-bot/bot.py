import asyncio
import logging
import os
from aiogram import Bot, Dispatcher

from handlers import start, poll, notes, remind
from db import init_db

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("токен") 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(poll.router)
dp.include_router(notes.router)
dp.include_router(remind.router)

async def main():
    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
