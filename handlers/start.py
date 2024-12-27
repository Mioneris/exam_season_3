from aiogram import Router, types
from aiogram.filters import Command
from .keyboards import complaint_keyboard

start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name

    await message.answer(f'Приветствуем тебя, {name}!\n'
                         f'Ниже предоставлен функионал нашего бота',
                         reply_markup=complaint_keyboard())
