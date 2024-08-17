import logging
from fastapi import APIRouter, Request
from aiogram.types import Update
from app.bot import bot, dp
from app.config import WEBHOOK_DOMAIN

webhook_route = APIRouter()

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

@webhook_route.post("/")
async def webhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot, update)