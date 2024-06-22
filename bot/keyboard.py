from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
        [KeyboardButton(text="Кнопка 3"), KeyboardButton(text="Кнопка 4")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Сделайте выбор...',
    selective=True,
)

second_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='InlineButton 1', callback_data='inline_button 1 callback')],
        [InlineKeyboardButton(text='InlineButton 2', callback_data='inline_button 2 callback')],
    ]
)
