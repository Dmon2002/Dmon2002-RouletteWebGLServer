import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import WebAppInfo
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBAPP_URL = os.getenv("WEBAPP_URL")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.button(text="🎮 Играть", web_app=WebAppInfo(url=WEBAPP_URL))
    builder.adjust(1)
    await message.answer("Привет! Нажми кнопку ниже, чтобы поиграть 👇", reply_markup=builder.as_markup(resize_keyboard=True))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
