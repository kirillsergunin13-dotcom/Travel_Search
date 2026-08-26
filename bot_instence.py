import telebot
from telebot.storage import StateMemoryStorage

BOT_TOKEN = "8908310695:AAFyUnDBRJ-jeacViGXKHWkhzIywdC3zO7k"

# Создаём единственный экземпляр TeleBot для всего приложения.
bot = telebot.TeleBot(
    BOT_TOKEN,
    # Состояния диалога хранятся в оперативной памяти. После перезапуска
    # программы они сбросятся, что допустимо для учебного проекта.
    state_storage=StateMemoryStorage(),
    # Разрешаем middleware-классы, в том числе StateMiddleware из main.py.
    use_class_middlewares=True,
)