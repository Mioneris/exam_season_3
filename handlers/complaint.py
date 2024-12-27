from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, types
from aiogram.types import CallbackQuery
import datetime
from bot_config import database

complaint_router = Router()


class Complaint(StatesGroup):
    name = State()
    contact_info = State()
    complaint = State()


@complaint_router.callback_query(F.data == 'complaint')
async def complaint_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Вы приступили к составлению жалобы.')
    await callback.message.answer('Как Вас зовут?')
    await callback.answer()

    await state.set_state(Complaint.name)


@complaint_router.message(Complaint.name)
async def get_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    if not name.isalpha():
        await message.answer("Пожалуйста, используйте буквы для ввода имени.Спасибо!")
        return

    await state.update_data(name=name)
    await message.answer('Пожалуйста, уточните контактную информацию для обратной связи.\n'
                         'Контактный номер телефона/инстаграм')
    await state.set_state(Complaint.contact_info)


@complaint_router.message(Complaint.contact_info)
async def get_contact_info(message: types.Message, state: FSMContext):
    contact_info = message.text.strip()
    await state.update_data(contact_info=contact_info)

    await message.answer('Пожалуйста, опишите нам ситуацию с которой Вы столкнулись.\n'
                         '(До 300 символов)')
    await state.set_state(Complaint.complaint)


@complaint_router.message(Complaint.complaint)
async def get_complaint(message: types.Message, state: FSMContext):
    complaint = message.text.strip()
    if len(complaint) > 300:
        await message.answer('Ограничение - 300 символов.')
        return

    await state.update_data(complaint=complaint)
    complaint_date = datetime.datetime.now().strftime('%d.%m.%Y')
    await state.update_data(complaint_date=complaint_date)

    data = await state.get_data()
    database.save_complaint(data)
    await message.answer('Жалоба сохранена.\n'
                         'Ожидайте обратной связи.')
    await state.clear()
