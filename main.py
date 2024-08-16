from os import getenv
import dotenv
import aiogram

# Load secrets from environment
dotenv.load_dotenv()

# Load Telegram bot API token
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")

# Load public domain for webhooks
PUBLIC_DOMAIN = getenv("PUBLIC_DOMAIN")

print(PUBLIC_DOMAIN)
