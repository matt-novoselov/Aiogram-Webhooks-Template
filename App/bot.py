from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer('Hello, world!')