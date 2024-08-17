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


async def set_webhook_if_needed():
    webhook_info = await bot.get_webhook_info()
    current_webhook_url = webhook_info.url

    # Check if the webhook is already set to the desired domain
    if current_webhook_url != f"{WEBHOOK_DOMAIN}/webhook":
        await bot.set_webhook(url=f"{WEBHOOK_DOMAIN}/webhook",
                              allowed_updates=dp.resolve_used_update_types(),
                              drop_pending_updates=True)
        logging.info(f"Webhook updated to: {WEBHOOK_DOMAIN}/webhook")
    else:
        logging.info("Webhook is already correctly set.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure the correct webhook is set when the app starts
    await set_webhook_if_needed()
    yield
    # Cleanup the webhook when the app stops
    await bot.delete_webhook()
    logging.info("Webhook deleted.")


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    uvicorn.run(app, host="0.0.0.0", port=8080)
