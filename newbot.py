import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


import patterns1



async def main():
    logging.basicConfig(level = logging.INFO)
        
    
    
    bot = Bot(token = "6791721652:AAEB37HY-SbGulUQeq2Q-xYnAQ2_iGj-bNk")
    dp = Dispatcher(storage=MemoryStorage())
    

    dp.include_router(router = patterns1.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())