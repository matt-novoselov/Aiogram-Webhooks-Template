import logging
from fastapi import APIRouter, Request, HTTPException
from aiogram.types import Update
from app.bot import bot, dp
from app.config import WEBHOOK_DOMAIN


# Create a new router
webhook_route = APIRouter()


# Set up a webhook on Telegram server
async def set_webhook():
    webhook_info = await bot.get_webhook_info()
    current_webhook_url = webhook_info.url

    # Check if the webhook is already set to the desired domain
    if current_webhook_url != WEBHOOK_DOMAIN:
        await bot.set_webhook(url=WEBHOOK_DOMAIN,
                              allowed_updates=dp.resolve_used_update_types(),
                              drop_pending_updates=True)
        logging.info(f"Webhook updated to: {WEBHOOK_DOMAIN}")
    else:
        logging.info("Webhook is already correctly set.")


# Delete webhook on telegram server
async def delete_webhook():
    await bot.delete_webhook()
    logging.info("Webhook deleted.")


# Webhook processing
async def webhook(request: Request) -> None:
    try:
        # Parse the incoming JSON payload from the request
        update = Update.model_validate(await request.json(), context={"bot": bot})
        await dp.feed_update(bot, update)
    except Exception as e:
        # Log any errors that occur while processing the update
        logging.error(f"Error handling update: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
