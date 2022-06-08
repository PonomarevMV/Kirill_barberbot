from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from datetime import datetime, timedelta
import calendar


calendar_callback = CallbackData('simple_calendar', 'act', 'year', 'month', 'day')

class SimpleCalendar:

    async def simple_start(self, year = int(datetime.now().year), month = int( datetime.now().month)):
        ignore_callback = calendar_callback.new("IGNORE", year, month, 0)

        inline_kb = InlineKeyboardMarkup(row_width = 7)
        inline_kb.row()
        inline_kb.insert(InlineKeyboardButton('<', callback_data=calendar_callback.new("PREV-MONTH", year, month, 1)))
        inline_kb.insert( InlineKeyboardButton(f'{calendar.month_name[month]} {str(year)}',callback_data = ignore_callback))
        inline_kb.insert( InlineKeyboardButton('>', callback_data=calendar_callback.new("NEXT-MONTH", year, month, 1)))


        inline_kb.row()
        for day in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Cб', 'Вс']:
            inline_kb.insert( InlineKeyboardButton(day, callback_data= ignore_callback))

        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            inline_kb.row()
            for day in week:
                if day == 0:
                    inline_kb.insert(InlineKeyboardButton(' ', callback_data= ignore_callback))
                    continue
                inline_kb.insert( InlineKeyboardButton( str(day), callback_data=calendar_callback.new("DAY", year, month, day) ))
        return inline_kb
    
    async def process_selection(self, query: CallbackQuery, data : CallbackData):
        return_data = (False, None)
        temp_date = datetime(int(data['year']), int(data['month']), 1)
    
        if data['act'] == 'IGNORE':
            await query.answer( cache_time=60 )
        if data['act'] == 'DAY':
            await query.message.delete_reply_markup()
            return_data = True, datetime(int(data['year']), int(data['month']), int(data['day']))

        if data['act'] == 'PREV-MONTH':
            prev_date = temp_date - timedelta(days = 1)
            await query.message.edit_reply_markup(await SimpleCalendar().simple_start(int(data['year']), int(prev_date.month)))
        if data['act'] == 'NEXT-MONTH':
            next_date = temp_date + timedelta(days=31)
            await query.message.edit_reply_markup(await SimpleCalendar().simple_start(int(data['year']), int(next_date.month)))
        return return_data
