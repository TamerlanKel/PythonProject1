from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())
kb = InlineKeyboardMarkup(resize_keyboard=True)
button1 = InlineKeyboardButton(text = 'Рассчитать', callback_data='calories')
button2 = InlineKeyboardButton(text = 'Формулы рассчета', callback_data='formulas')
kb.add(button1, button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()





@dp.message_handler(commands=['start'])
async def start(message):
    reply_markup = kb
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    reply_markup = kb
    await message.answer('Выберите опцию:', reply_markup=kb)



@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    formula = "10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5"
    await call.message.answer(formula)
    await call.answer()

@dp.message_handler(text = 'Информация')
async def inform(message):
    await message.answer('Информация о боте!')


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()



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