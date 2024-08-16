from os import getenv
import dotenv
import aiogram

# Load secrets from environment
dotenv.load_dotenv()

# Load Telegram bot API token
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
