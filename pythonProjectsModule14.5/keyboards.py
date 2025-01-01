from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text = 'Витамин D3 5000 МЕ', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'Креатин', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'Протеин', callback_data='product_buying')],
        [InlineKeyboardButton(text = 'БЦА', callback_data='product_buying')]
    ], resize_keyboard=True
)


info_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Рассчитать"),
            KeyboardButton(text="Информация")
        ],
        [
            KeyboardButton(text="Купить")
        ],
        [
            KeyboardButton(text="Регистрация")
        ]
    ],
    resize_keyboard=True
)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Пользователи", callback_data="users")],
        [InlineKeyboardButton(text="Статистика", callback_data="stat")],
        [
        InlineKeyboardButton(text="Блокировка", callback_data="block"),
        InlineKeyboardButton(text="Разблокировка", callback_data="unblock")
        ]
    ]
)