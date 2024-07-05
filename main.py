import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import TOKEN, OPENWEATHERMAP_API_KEY
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def get_weather(city: str) -> str:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHERMAP_API_KEY}&units=metric'

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    weather_main = data['weather'][0]['main']
                    weather_description = data['weather'][0]['description']
                    temperature = data['main']['temp']
                    city_name = data['name']
                    country = data['sys']['country']

                    return f"Сейчас в {city_name}, {country} температура: {temperature}°C, погодные условия: {weather_description}."
                else:
                    return f"Ошибка при получении данных о погоде: {response.status} - {await response.text()}"
    except aiohttp.ClientError as ce:
        return f"Ошибка соединения: {ce}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

@dp.message(Command("weather"))
async def weather(message: Message):
    try:
        # Извлечение названия города из сообщения
        city = message.text.split(maxsplit=1)[1]
        weather_info = await get_weather(city)
        await message.answer(weather_info)
    except IndexError:
        await message.answer("Пожалуйста, укажите название города. Пример: /weather Moscow")

@dp.message(Command('photo'))
async def photo(message: Message):
    photo_list = ['https://s1.1zoom.ru/big3/984/Canada_Parks_Lake_Mountains_Forests_Scenery_Rocky_567540_3840x2400.jpg',
                  'https://yandex.ru/images/search?pos=17&text=%D1%84%D0%BE%D1%82%D0%BE&img_url=https%3A%2F%2Fuploads.myubi.tv%2Fwp-content%2Fuploads%2Fanswers%2F16192%2F2HUM4BZY5Jpic.jpg&rpt=simage&source=serp&lr=197',
                  'https://yandex.ru/images/search?pos=31&text=%D1%84%D0%BE%D1%82%D0%BE&img_url=https%3A%2F%2Fwww.zastavki.com%2Fpictures%2F1920x1200%2F2011%2FNature_Other_Beautiful_scenery_031215_.jpg&rpt=simage&source=serp&lr=197']
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.photo)
async def react_photo(message: Message):
    text_list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(text_list)
    await message.answer(rand_answ)

@dp.message(F.text == "что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды: \n/start \n/help \n/photo \n /weather")

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет, я бот!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
