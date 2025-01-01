from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from texts import *
from keyboards import *
from admin import *
from crud_functions import get_all_products
from crud_functions import *
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage= MemoryStorage())


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    reply_markup = info_kb
    await message.answer(start_work, reply_markup=info_kb)


@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await RegistrationState.username.set()
    await message.answer('Введите имя пользователя (только латинский алфавит)', reply_markup=info_kb)


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    username = message.text
    user_ex = is_included(username)
    if user_ex:
        await message.answer('Пользователь существует, введите другое имя')
        return
    else:
        await state.update_data(username=username)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
        return


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    email = message.text
    await state.update_data(email=email)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    age = int(message.text)
    await state.update_data(age=age)
    user_data = await state.get_data()  # Добавляем await перед вызовом get_data()
    username = user_data['username']
    email = user_data['email']
    age = user_data['age']
    add_user(username, email, age)  # Передаем все данные в add_user
    await message.answer('Регистрация прошла успешно!')
    await state.finish()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    reply_markup = info_kb
    await message.answer('Выберите опцию:', reply_markup=info_kb)



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

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    products = get_all_products()
    with open('1.png', "rb") as img:
        await message.answer_photo(img, f"Название: Vitamin D3 | Описание: {vitamin_D3} | Цена: 873")
    with open('2.png', "rb") as img:
        await message.answer_photo(img, f"Название: Creatine | Описание: {creatine} | Цена: 1800")
    with open('3.png', "rb") as img:
        await message.answer_photo(img, f"Название: Protein | Описание: {protein} | Цена: 3000")
    with open('4.png', "rb") as img:
        await message.answer_photo(img, f"Название: BCAA | Описание: {bcaa} | Цена: 1000")
    await message.answer("Выберите продукт для покупки:", reply_markup=catalog_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer(all_messages)

if __name__ == "__main__":
    initiate_db()
    data()
    executor.start_polling(dp, skip_updates=True)