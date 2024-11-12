from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
# Token хранится в файле config.py
from config import TOKEN

# Задача "Цепочка вопросов"

api = TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


# Объявляю класс состояний
class UserState(StatesGroup):
    # Состояние "Возраст"
    age = State()
    # Состояние "Рост"
    growth = State()
    # Состояние "Вес"
    weight = State()


# Обработка сообщения "Calories"
@dp.message_handler(text='Calories')
async def set_age(message):
    # Запрос возраста у пользователя
    await message.answer('Введите свой возраст (целое число) в годах:')
    # Установка состояния возраста
    await UserState.age.set()

# Обработка сообщения с возрастом
@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    # Проверка значения возраста на соответствие целому числу
    if message.text.isdigit():
        # Сохраняю состояние возраста
        await state.update_data(age=int(message.text))
        # Запрос роста у пользователя
        await message.answer('Введите свой рост (целое число) в сантиметрах:')
        # Установка состояния роста
        await UserState.growth.set()
    else:
        await message.answer('Неверное значение. Введите свой возраст в годах:')


# Обработка сообщения с ростом
@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    # Проверка значения роста на соответствие целому числу
    if message.text.isdigit():
        # Сохраняю состояние роста
        await state.update_data(growth=int(message.text))
        # Запрос веса у пользователя
        await message.answer('Введите свой вес (целое число) в килограммах:')
        # Установка состояния веса
        await UserState.weight.set()
    else:
        await message.answer('Неверное значение. Введите свой рост в сантиметрах:')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    # Проверка значения веса на соответствие целому числу
    if message.text.isdigit():
        # Сохраняю состояние веса
        await state.update_data(weight=int(message.text))
        # Формирую словарь для записи адреса и передаю в него данные из состояния
        data = await state.get_data()
        # Рассчёт калорий для мужчин и для женщин
        male_gender: float = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] + 5
        female_gender: float = 10 * data['weight'] + 6.25 * data['growth'] - 5 * data['age'] - 161
        # Формирую текст ответа
        answer_text: str = ('Согласно упрощенному варианту формулы Миффлина-Сан Жеора, для оптимального похудения или '
                            'сохранения нормального веса, Вам необходимо килокалорий (ккал) в сутки:\n' +
                            str(male_gender) + ' (для мужчин)\n' + str(female_gender) + ' (для женщин)')
        # Отправляю пользователю текст с рассчитанным значением калорий
        await message.answer(answer_text)
        # Закрываю машину состояний
        await state.finish()
    else:
        await message.answer('Неверное значение. Введите свой вес в килограммах:')


# Подпись отправителя сообщения
def sender_sign(message):
    sign_str: str = (message['from']['username'] + ' (' +
                     message['from']['last_name'] + ' ' +
                     message['from']['first_name'] + ')')
    return sign_str


# Обработка команды '/start'
@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет {sender_sign(message)}!\n'
                         'Я бот, помогающий твоему здоровью.\n'
                         'Отправьте слово Calories для подсчёта калорий')


# Обработка всех остальных сообщений и команд
@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
