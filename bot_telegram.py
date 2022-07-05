import os
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, reply_keyboard
from aiogram.utils import executor
from aiogram.utils.callback_data import CallbackData
from create_bot import dp, bot
from keyboards import simple_cal_callback, SimpleCalendar, selected_time, chose_service
from base_date import sql_date
from handlers.client_handlers import register_handler_client
import config


async def on_startup(dp):
    print("Бот вышел в онлайн")
    sql_date.sql_start()
    await bot.set_webhook(config.URL_APP)

async def on_shutdown(dp):
    await bot.delete_webhook()


register_handler_client( dp )

'''
@dp.message_handler(commands=['start'])
async def cmd_start(message: Message):
    await message.answer("Please enter a date for zapis", reply_markup= start_kb)
    #await message.reply("Please put down the button \'calendar\'", reply_markup= await SimpleCalendar().start_calendar())

@dp.message_handler(Text (equals=['Calendar'], ignore_case= True))
async def show_calendar(message: Message):
    await message.answer('Please select a date', reply_markup= await SimpleCalendar().simple_start())  

@dp.callback_query_handler(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
   selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
   if selected:
       await callback_query.message.answer(f'Please selected service', reply_markup=await chose_service())
       await callback_query.message.delete()

@dp.callback_query_handler(text = 'service')
async def process_selected_service(callback_query: CallbackQuery):
    await callback_query.message.answer('Please selected time to vizit', reply_markup= await selected_time())
    await callback_query.message.delete_reply_markup()
    await callback_query.message.delete()

@dp.callback_query_handler(text= 'you chose time')
async def answer (callback_query: CallbackQuery):
    await callback_query.message.answer(text = 'You writen to vizit, thnks for user our app!')
    await callback_query.message.delete_reply_markup()
    await callback_query.message.delete()
    #await callback_query.answer(text = 'You writen to vizit, thnks for user our app!')
'''

executor.start_webhook(
    dispatcher= dp,
    webhook_path='',
    on_startup= on_startup,
    on_shutdown= on_shutdown,
    skip_updates= True,
    host= "0.0.0.0",
    port= int(os.environ.get("PORT", 5000)))
