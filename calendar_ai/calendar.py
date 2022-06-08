import calendar
from datetime import datetime, timedelta
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.utils.callback_data import CallbackData
from aiogram.types import CallbackQuery



calendar_callback = CallbackData('simple_calendare', 'act', 'year', 'mont', 'day')

class SimpleCalendar:

    async def start_calendar(self, year: int = datetime.now().year, month: int = datetime.now().month):
        
        button_kb = ReplyKeyboardMarkup(resize_keyboard = True)
        ignore_callback = calendar_callback.new("IGNORE", year, month, 0)
        button_kb.row()
        button_kb.insert( KeyboardButton("<", callback_data=calendar_callback.new("PREV-YEAR", year, month, 1)))



