#py mft-main.py
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "" #pls write your telegram bott api in string format
bot = Bot(TOKEN)
dp = Dispatcher()
global a
waiting_for_message = {}

async def start_in_group(message: types.Message):
    waiting_for_message[message.from_user.id] = True

dp.message.register(start_in_group, Command(commands=["start"]))

async def new_message(message: types.Message):
    if waiting_for_message.get(message.from_user.id):
        waiting_for_message[message.from_user.id] = False
        a = message.text
        await message.answer(a)

dp.message.register(new_message)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot, skip_updates=True))
