import os
import random
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from gtts import gTTS
from googletrans import Translator
from config import TOKEN

# Создаем папку img, если ее не существует
if not os.path.exists("img"):
    os.makedirs("img")

bot = Bot(token=TOKEN)
dp = Dispatcher()

translator = Translator()

@dp.message(F.photo)
async def save_photo(message: Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path

    # Скачиваем файл и сохраняем в папке img
    file_name = f"img/{file_id}.jpg"
    await bot.download_file(file_path, file_name)

    await message.answer("Фото сохранено.")

@dp.message(Command('voice'))
async def send_voice(message: Message):
    tts = gTTS(text="Это тестовое голосовое сообщение.", lang='ru')
    tts.save("voice_message.ogg")

    voice = FSInputFile("voice_message.ogg")
    await message.answer_voice(voice)

    # Удаляем файл после отправки
    os.remove("voice_message.ogg")

@dp.message(F.text)
async def translate_text(message: Message):
    translated = translator.translate(message.text, src='ru', dest='en')
    await message.answer(f"Перевод: {translated.text}")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
