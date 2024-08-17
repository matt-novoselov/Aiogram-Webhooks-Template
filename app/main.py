import logging
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.webhook import set_webhook_if_needed, webhook
from app.bot import bot


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure the correct webhook is set when the app starts
    await set_webhook_if_needed()
    yield
    # Cleanup the webhook when the app stops
    await bot.delete_webhook()
    logging.info("Webhook deleted.")

app = FastAPI(lifespan=lifespan)

# Directly add the webhook route to the FastAPI app
app.add_api_route("/", webhook, methods=["POST"])

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
