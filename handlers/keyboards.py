from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def complaint_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Жалоба', callback_data='complaint'),
            ]
        ]
    )
