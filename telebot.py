import asyncio
import logging
import sys
from os import getenv
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
import string
import random

TOKEN = getenv('your token')
dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Введите длину пароля, который необходимо создать")

@dp.message()
async def echo_handler(message: types.Message) -> None:
    if message.text == "нет" or message.text == "Нет":
        await message.answer("Досвидания")
    else:      
        characters = string.ascii_letters + string.digits + string.punctuation
        t = int(message.text)
        password = "".join(random.choice(characters) for _ in range(t))
        await message.answer(password)
        await message.answer('Сгенерировать ещё один пароль? Если да, то введите количество символов в новом пароле. В противном случае введите "Нет"')
    
async def main() -> None:
    bot = Bot(token='6802985071:AAFBsghyq8ofvKgiu_UHehA9rdhf8uLRedk')
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
