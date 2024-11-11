from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Token хранится в файле config.py
from config import TOKEN

# Задача "Бот поддержки (Начало)"

api = TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Подпись отправителя сообщения
def sender_sign(message):
    sign_str: str = (message['from']['username'] + ' (' +
                     message['from']['last_name'] + ' ' +
                     message['from']['first_name'] + ')')
    return sign_str


# Обработка сообщения 'Urban'
@dp.message_handler(text=['Urban'])
async def urban_message(message):
    await message.answer('Urban message!')


# Обработка команды '/start'
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет {sender_sign(message)}! Я бот помогающий твоему здоровью.')


# Обработка всех остальных сообщений и команд
@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
