import os
# импортируем модуль emoji для отображения эмоджи
from emoji import emojize

# токен выдается при регистрации приложения
TOKEN = '6778261614:AAG5InesmBEvnLHTie4yQVDk4tgdRtvDQgY'
# название БД
NAME_DB = 'products.db'
# версия приложения
VERSION = '1.1.3'
# автор приложния
AUTHOR = 'odani'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize(':open_file_folder: Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'virtual_number': emojize('📱 Виртуальные номера'),
    'accounts': emojize('💻 Аккаунты с играми'),
    'subscriptions': emojize('🎮 Подписки на сервисы'),
    'nft' : emojize ('🖌 Цифровое искусство'),
    '<<': emojize('⬅'),
    '>>': emojize('➡'),
    'BACK_STEP': emojize('◀'),
    'NEXT_STEP': emojize('▶'),
    'ORDER': emojize('🗑️'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅➡🗑️',
    'COPY': '©️'
}

# id категорий продуктов
CATEGORY = {
    'virtual_number': 1,
    'accounts': 2,
    'subscriptions': 3,
    'nft' : 4,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
