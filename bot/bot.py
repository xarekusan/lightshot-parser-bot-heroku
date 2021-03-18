import logging

from shutil import rmtree
from os import remove
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_webhook
from aiogram.types import ReplyKeyboardMarkup, \
                        KeyboardButton
from bot.this_is_script import start_script
from bot.settings import (BOT_TOKEN, HEROKU_APP_NAME,
                          WEBHOOK_URL, WEBHOOK_PATH,
                          WEBAPP_HOST, WEBAPP_PORT)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

btn_parsing = KeyboardButton("/parsing")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_parsing)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет!\nНажми на кнопку ниже, чтобы начать парсинг",
                           reply_markup=greet_kb)


@dp.message_handler(commands=["parsing"])
async def parsing(message: types.Message):
    filename = start_script()
    with open(filename, 'rb') as photo:
        try:
            await bot.send_photo(chat_id=message.chat.id, photo=photo)
        except Exception:
            await bot.send_message(chat_id=message.chat.id, text="Error. Try again")
    remove(filename)
    rmtree('.cache', ignore_errors=True)


async def on_startup(dp):
    logging.warning(
        'Starting connection. ')
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


async def on_shutdown(dp):
    logging.warning('Bye! Shutting down webhook connection')


def main():
    logging.basicConfig(level=logging.INFO)
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
