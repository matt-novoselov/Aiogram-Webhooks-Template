# Aiogram Webhooks Template

Template for Aiogram 3.x-based Webhooks Telegram bot.

## Requirements
- Python 3.8
- aiogram 3.12.0
- python-dotenv 1.0.1
- fastapi 0.112.1
- uvicorn 0.30.6

## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/Aiogram-Webhooks-Template.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - TELEGRAM_TOKEN: Insert your Telegram Bot Token obtained from the [BotFather](https://t.me/botfather).
   - WEBHOOK_DOMAIN: Public SSL domain that will be listening for webhooks request from Telegram.
4. Build and run `main.py`

<br>

Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
