from os import getenv
import dotenv
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message, Update
from aiogram.filters import CommandStart
from fastapi import FastAPI, Request
import uvicorn
from contextlib import asynccontextmanager

# Load secrets from environment
dotenv.load_dotenv()
# Load Telegram bot API token
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
# Load public domain for webhooks
WEBHOOK_DOMAIN = getenv("WEBHOOK_DOMAIN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer('Hello, world!')




@asynccontextmanager
async def lifespan(app: FastAPI):
    await bot.set_webhook(url=f"{WEBHOOK_DOMAIN}/webhook",
                          allowed_updates=dp.resolve_used_update_types(),
                          drop_pending_updates=True)
    yield
    await bot.delete_webhook()

app = FastAPI(lifespan=lifespan)

@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    print(await request.json())
    await dp.feed_update(bot, update)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    uvicorn.run(app, host="0.0.0.0", port=8080)
