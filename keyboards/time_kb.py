from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from datetime import timedelta, datetime, time
from aiogram.utils.callback_data import CallbackData


time_callback_data = CallbackData( 'Time', 'time')

async def selected_time( state ):
    work_time = state[0] + timedelta( hours=11 )
    end_work_time = state[0] + timedelta ( hours= 20 )
    if state[1] == 'Model heircut':
        time_kn = InlineKeyboardMarkup( row_width= 5 )
        while work_time <= end_work_time:
            time_kn.insert (InlineKeyboardButton( text= f'{work_time.strftime("%H.%M")}', callback_data= time_callback_data.new( work_time.strftime("%H.%M") ) ))
            work_time = work_time + timedelta( hours= 1 ) + timedelta( minutes= 30 )
        return time_kn

    if state[1] == 'Machine heircut':
        time_kn = InlineKeyboardMarkup( row_width= 5 )
        while work_time <= end_work_time:
            time_kn.insert (InlineKeyboardButton( text= f'{work_time.strftime("%H.%M")}', callback_data= time_callback_data.new( work_time.strftime("%H.%M") ) ))
            work_time = work_time + timedelta( hours= 1 )
        return time_kn      

    if state[1] == 'Beard modeling':
        time_kn = InlineKeyboardMarkup( row_width= 5 )
        while work_time <= end_work_time:
            time_kn.insert (InlineKeyboardButton( text= f'{work_time.strftime("%H.%M")}', callback_data= time_callback_data.new( work_time.strftime("%H.%M") ) ))
            work_time = work_time + timedelta( hours= 1 )
        return time_kn


    '''
    time_kn = InlineKeyboardMarkup( row_width=7)
    for time in ['11:00', '12:30', '14:00', '15:30', '17:00', '18:30', '20:00']:
        time_kn.insert( InlineKeyboardButton(text = f'{time}', callback_data = 'you chose time'))
    return time_kn
'''

