from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, CallbackData

main = ReplyKeyboardMarkup(keyboard=[
   [KeyboardButton(text="Тестовая кнопка 1")],
   [KeyboardButton(text="Тестовая кнопка 2"), KeyboardButton(text="Тестовая кнопка 3")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Видео", url='https://www.youtube.com/watch?v=HfaIcB4Ogxk')],
   [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
   [InlineKeyboardButton(text="Новости", callback_data='news')],
   [InlineKeyboardButton(text="Профиль", callback_data='person')]
])


test = ["кнопка 1", "кнопка 2", "кнопка 3", "кнопка 4"]

async def test_keyboard():
   keyboard = InlineKeyboardBuilder()
   for key in test:
       keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
   return keyboard.adjust(2).as_markup() # создаются под сообщением

# async def test_keyboard():
#    keyboard = ReplyKeyboardBuilder()
#    for key in test:
#        keyboard.add(KeyboardButton(text=key))
#    return keyboard.adjust(2).as_markup() # создаются под строкой запроса

# для домашнего задания
main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Привет")],
    [KeyboardButton(text="Пока")]
], resize_keyboard=True)

# Создаем инлайн-клавиатуру с URL-кнопками
inline_keyboard_links = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Новости", url='https://ria.ru')],
    [InlineKeyboardButton(text="Музыка", url='https://music.youtube.com/watch?v=yUp01GbQxTw&list=OLAK5uy_n8mWiOJozXA7wqNc7o31BbBOczHuxedb4')],
    [InlineKeyboardButton(text="Видео", url='https://www.ivi.ru/movies/2024')]
])

# Кнопка "Показать больше"
inline_dynamic = InlineKeyboardMarkup(inline_keyboard=[
   [InlineKeyboardButton(text="Показать больше", callback_data='dynamic')],
])

# Кнопки "Опция 1" и "Опция 2"
async def dynamic_keyboard():
   keyboard = InlineKeyboardBuilder()
   options = ["Опция 1", "Опция 2"]
   for key in options:
       keyboard.add(InlineKeyboardButton(text=key, callback_data=key))
   return keyboard.adjust(1).as_markup()

