from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


callback_service = CallbackData ('Service', 'service')

async def chose_service():
    chose_service = InlineKeyboardMarkup(row_width= 3)
    b1 = InlineKeyboardButton(text= 'Model heircut', callback_data= callback_service.new( 'Model heircut' ) )
    b2 = InlineKeyboardButton(text = 'Machine heircut', callback_data= callback_service.new( 'Machine heircut' ))
    b3 = InlineKeyboardButton(text = 'Beard modeling', callback_data=callback_service.new( 'Beard modeling' ))
    chose_service.add(b1, b2, b3)
    return chose_service