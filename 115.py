import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from config import TOKEN
import keyboard_script as kb

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}', reply_markup=kb.main_keyboard)

@dp.message(F.text == "Привет")
async def greet(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

@dp.message(F.text == "Пока")
async def farewell(message: Message):
    await message.answer(f'До свидания, {message.from_user.first_name}!')

@dp.message(Command('links'))
async def send_links(message: Message):
    await message.answer("Вот несколько ссылок:", reply_markup=kb.inline_keyboard_links)

@dp.message(Command('dynamic'))
async def dynamic(message: Message):
    await message.answer('Показать больше', reply_markup=kb.inline_dynamic)

@dp.callback_query(F.data == 'dynamic')
async def show_options(callback: CallbackQuery):
    await callback.message.edit_text('Выберите опцию:', reply_markup=await kb.dynamic_keyboard())

@dp.callback_query(F.data.in_({'Опция 1', 'Опция 2'}))
async def handle_option(callback: CallbackQuery):
    await callback.message.answer(f'Вы выбрали {callback.data}')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
