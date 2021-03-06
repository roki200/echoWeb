import logging
from aiogram import types
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import bot, dp, WEBHOOK_PATH, WEBHOOK_URL, WEBAPP_PORT
from db import database


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)
    logging.warning('Вебхук подключён.')
    #await database.connect() это бд той статьи 


async def on_shutdown(dp):
    logging.warning('Вебхук отключён.')
    #await database.disconnect() это бд той статьи


async def on_startup(dispatcher):
    await database.connect()
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dispatcher):
    await database.disconnect()
    await bot.delete_webhook()


CREATE TABLE messages (
id SERIAL PRIMARY KEY,
telegram_id INTEGER NOT NULL,
text text NOT NULL
);


async def save(user_id, text):
    await database.execute(f"INSERT INTO messages(telegram_id, text) "
                           f"VALUES (:telegram_id, :text)", values={'telegram_id': user_id, 'text': text})


async def read(user_id):
    results = await database.fetch_all('SELECT text '
                                       'FROM messages '
                                       'WHERE telegram_id = :telegram_id ',
                                       values={'telegram_id': user_id})
    return [next(result.values()) for result in results]


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет,напиши мне что нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне сообщение и  отправлю тебе в ответ!")


@dp.message_handler(commands=['owner'])
async def process_help_command(message: types.Message):
    await message.reply("Мой создатель👨‍💻 @roki_crayzy,15 y.o , 🇷🇺/🇹🇯")
                 

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_chat.id, msg.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host='0.0.0.0',
        port=WEBAPP_PORT,
    )
