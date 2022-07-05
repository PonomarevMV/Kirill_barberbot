from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
import config

bot = Bot(token = config.TOKEN)
dp = Dispatcher(bot)