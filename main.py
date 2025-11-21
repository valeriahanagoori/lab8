from aiogram import *
import asyncio
import logging
from aiogram.filters import Command
from dotenv import load_dotenv
import os


API_TOKEN =''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Самый лучший бот!\nОтправь мне любое сообщение, и я тебе отвечу.")

@dp.message_handler()
async def echo(message: types.Message):
 await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

