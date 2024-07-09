from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import logging
from config import TOKEN, exchangerate_api
import requests
import asyncio

# Инициализация бота
bot = Bot(token=TOKEN)

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Ключ API для конвертации валют
EXCHANGE_API_KEY = exchangerate_api

# Инициализация диспетчера и роутера
dp = Dispatcher()
router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я твой помощник. Я могу конвертировать валюты. Используй команду /convert.")

# Обработчик команды /convert
@router.message(Command("convert"))
async def convert_currency(message: types.Message):
    params = message.text.split()
    if len(params) != 4:
        await message.reply(
            "Использование: /convert amount from_currency to_currency\nПример: /convert 100 USD EUR")
        return

    amount, from_currency, to_currency = params[1], params[2], params[3]
    url = f'https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{from_currency}'
    response = requests.get(url)
    exchange_data = response.json()

    if exchange_data['result'] == 'success':
        rate = exchange_data['conversion_rates'].get(to_currency)
        if rate:
            converted_amount = float(amount) * rate
            await message.reply(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        else:
            await message.reply(f"Валюта {to_currency} не найдена.")
    else:
        await message.reply("Не удалось выполнить конвертацию. Проверьте введенные данные и попробуйте снова.")

# Асинхронная функция для запуска бота
async def main():
    # Регистрация роутеров
    dp.include_router(router)

    # Запуск бота
    await dp.start_polling(bot)

# Запуск асинхронной функции main с помощью asyncio
if __name__ == "__main__":
    asyncio.run(main())