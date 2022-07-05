from aiogram import Dispatcher, types
from keyboards import start_client, SimpleCalendar, simple_cal_callback, chose_service, selected_time
from aiogram.types import CallbackQuery
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters import Text
from keyboards.service_kb import callback_service
from keyboards.time_kb import time_callback_data
from base_date import postgrepsql

#словарь для добавление выбора услуг клиента
user_service = {}

#Хендлер отлавливающий старт бота
#@dp.message_handler (commands = ['/start'])
async def start (message : types.Message):
    await message.answer("Hi, how are you?", reply_markup= await start_client())

#Показ календаря для выбора даты записи
#dp.message_handler (Text (equals=['Make an appointment'], ignore_case= True))
async def chouse_date (message : types.Message ):
    await message.answer('Please select a date', reply_markup= await SimpleCalendar().simple_start())

#Хэндлер отлавливающий нажатие кнопки "Мои записи"
#dp.message_handler ( Text (equals=['My entries'], ignore_case= True) )
async def my_entries( message: types.Message ):
    await postgrepsql.sql_read(message)

#Выбор даты в календаре и его запись в словарь
#@dp.callback_query_handler(simple_cal_callback.filter(), state = ClientService.chouse_date)
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict):
   selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
   if selected:
       user_service[ callback_query.from_user.id ] = [date, ]
       print ( user_service[ callback_query.from_user.id ] )
       await callback_query.message.answer(f'Please selected service', reply_markup=await chose_service())
       await callback_query.message.delete()

#Выбор услуги и запись в словарь, выбор времени
#@dp.callback_query_handler(state = ClientService.chouse_service)
async def process_selected_service(callback_query: CallbackQuery, callback_data: dict ):
    if callback_data['service'] == 'Model heircut':
        user_service[ callback_query.from_user.id].append('Model heircut')
    if callback_data['service'] == 'Machine heircut':
        user_service[ callback_query.from_user.id].append('Machine heircut')
    if callback_data['service'] == 'Beard modeling':
        user_service[ callback_query.from_user.id].append('Beard modeling')
    print( user_service )
    await callback_query.message.answer('Please selected time to vizit', reply_markup= await selected_time( user_service[ callback_query.from_user.id] ))
    await callback_query.message.delete_reply_markup()
    await callback_query.message.delete()

#Запись времени в словарь, запись в базу данных клиента.
#@dp.callback_query_handler(text= 'you chose time')
async def answer (callback_query: CallbackQuery, callback_data: dict ):
    await callback_query.message.answer(text = 'You writen to vizit, thnks for user our app!')
    user_service[ callback_query.from_user.id ].append( callback_data['time'] )
    print( user_service )
    await postgrepsql.sql_add_command( callback_query.from_user.id,  user_service[ callback_query.from_user.id ])
    await callback_query.message.delete_reply_markup()
    await callback_query.message.delete()


def register_handler_client( dp : Dispatcher ):
    dp.register_message_handler(start, commands = 'start')
    dp.register_message_handler( chouse_date, Text (equals=['Make an appointment'], ignore_case= True) )
    dp.register_message_handler( my_entries, Text (equals=['My entries'], ignore_case= True) )
    dp.register_callback_query_handler ( process_simple_calendar,  simple_cal_callback.filter()) 
    dp.register_callback_query_handler ( process_selected_service, callback_service.filter())
    dp.register_callback_query_handler ( answer, time_callback_data.filter() )