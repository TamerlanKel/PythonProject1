from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())
kb = ReplyKeyboardMarkup()
button1 = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.row(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()





@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup = kb)


@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Информация о боте!')


@dp.message_handler(text = 'Рассчитать')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()



@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await message.answer('Введите свой рост:')
    print(f'Возраст пользователя: {message.text}')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await message.answer('Введите свой вес:')
    print(f'Рост пользователя: {message.text}')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    print(f'Вес пользователя: {message.text}')
    data = await state.get_data()
    age = data.get('age')
    growth = data.get('growth')
    weight = data.get('weight')
    formula = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f'Норма калорий {formula}.')
    print(f'Норма калорий пользователя: {formula}')
    await state.finish()


@dp.message_handler()
async def all_message(message):
    print("Введите команду /start, чтобы начать общение")
    await message.answer("Введите команду /start, чтобы начать общение")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)