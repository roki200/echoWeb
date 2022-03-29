from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook
from config import bot, dp, WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT






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
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
