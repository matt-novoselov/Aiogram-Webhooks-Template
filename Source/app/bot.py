from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from Source.app.config import TELEGRAM_TOKEN

# Initialize bot
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


# /start command
@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer('Hello, world!')
