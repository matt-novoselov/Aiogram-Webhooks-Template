from os import getenv
import dotenv

# Load secrets from environment
dotenv.load_dotenv()

# Load Telegram bot API token
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
# Load public domain for webhooks
WEBHOOK_DOMAIN = getenv("WEBHOOK_DOMAIN")
