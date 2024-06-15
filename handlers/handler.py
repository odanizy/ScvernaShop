# реализация абстрактных классов
import abc
# разметка клавиатуры и клавиш
from markup.markup import Keyboards
# класс-менеджер для работы с библиотекой
from data_base.dbalchemy import DBManager


class Handler(metaclass=abc.ABCMeta):

    def __init__(self, bot):
        # получаем объект бота
        self.bot = bot
        # инициализируем разметку кнопок
        self.keybords = Keyboards()
        # инициализируем менеджер для работы с БД
        self.BD = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
