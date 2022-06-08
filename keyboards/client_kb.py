from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


async def start_client ():
    b1 = KeyboardButton( 'Make an appointment' )
    b2 = KeyboardButton (' My entries ')

    kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
    
    kb_client.add(b1, b2)

    return kb_client

