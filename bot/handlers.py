import logging

from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot.keyboard import main_keyboard, second_keyboard

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {message.from_user.full_name}!",
        reply_markup=main_keyboard
    )


@router.message(F.text == 'Кнопка 2')
async def button_2_handler(message: Message) -> None:
    await message.answer(
        'Вы выбрали кнопку 2, открывается inline клавиатура',
        reply_markup=second_keyboard
    )


@router.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
        logging.info(f'echo_handler : {message.text}')
    except TypeError:
        await message.answer("Nice try!")


@router.callback_query(F.data == 'inline_button 1 callback')
async def inline_button_1_handler(callback: CallbackQuery) -> None:
    await callback.answer('')
    await callback.message.answer(text='Ответ на коллбэк от inline_button 1')
