from aiogram.dispatcher import Dispatcher
from aiogram import Bot
import os


BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN, parse_mode='html', disable_web_page_preview=True)
dp = Dispatcher(bot)

# Настройки вебхука
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f"https://{os.getenv('HEROKU_APP_NAME')}.herokuapp.com{WEBHOOK_PATH}"
WEBAPP_PORT = int(os.getenv('PORT'))
