from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# Token хранится в файле config.py
from config import TOKEN

# Задача "Витамины для всех!"

products = [
    ['Витамин C', 'Антиоксидант', 'Vit_C.webp'],
    ['Витамин D3', 'Обмен кальция и фосфора', 'Vit_D.webp'],
    ['Витамин E', 'Замедляет старение клеток', 'Vit_E.webp'],
    ['Витамин Омега-3', 'Здоровье сердца и сосудов', 'Vit_Omega.webp']
]

api = TOKEN
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Клавиатура ReplyKeyboardMarkup
kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
bt_calc = KeyboardButton(text='Рассчитать')
bt_info = KeyboardButton(text='Информация')
bt_buy = KeyboardButton(text='Купить')
kb_main.add(bt_calc)
kb_main.insert(bt_info)
kb_main.insert(bt_buy)

# Клавиатура InlineKeyboardMarkup
kb_calc = InlineKeyboardMarkup()
bt_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
bt_formulas = InlineKeyboardButton(text='Формула расчёта', callback_data='formulas')
kb_calc.add(bt_calories)
kb_calc.add(bt_formulas)

# Клавиатура с продуктами
kb_buy = InlineKeyboardMarkup()
bt_product1 = InlineKeyboardButton(text=products[0][0], callback_data='product_buying')
bt_product2 = InlineKeyboardButton(text=products[1][0], callback_data='product_buying')
bt_product3 = InlineKeyboardButton(text=products[2][0], callback_data='product_buying')
bt_product4 = InlineKeyboardButton(text=products[3][0], callback_data='product_buying')
kb_buy.add(bt_product1)
kb_buy.insert(bt_product2)
kb_buy.insert(bt_product3)
kb_buy.insert(bt_product4)


# Подпись отправителя сообщения
def sender_sign(message):
    sign_str: str = (message['from']['username'] + ' (' +
                     message['from']['last_name'] + ' ' +
                     message['from']['first_name'] + ')')
    return sign_str


# Обработка команды '/start'
@dp.message_handler(commands='start')
async def start(message):
    await message.answer(f'Привет, {sender_sign(message)}!\n'
                         'Я бот, помогающий твоему здоровью.\n', reply_markup=kb_main)


# Обработка нажатия кнопки "Рассчитать"
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    # Запрос у пользователя ("Рассчитать норму калорий" или "Формула расчёта")
    await message.answer('Выберите опцию:', reply_markup=kb_calc)


# Обработка нажатия кнопки "Информация"
@dp.message_handler(text='Информация')
async def inform(message):
    info_text: str = ('Бот подскажет количество килокалорий (ккал), необходимое человеку в сутки.\nРассчёт калорий '
                      'ведётся по формуле Миффлина-Сан Жеора.\nЭто одна из самых последних формул расчета калорий для '
                      'оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и все '
                      'чаще стала заменять классическую формулу Харриса-Бенедикта.\nФормула Миффлина-Сан Жеора, '
                      'разработанная группой американских врачей-диетологов под руководством докторов Миффлина и Сан '
                      'Жеора, выдает необходимое количество килокалорий в сутки для каждого конкретного человека.')
    await message.answer(info_text)


# Обработка нажатия кнопки "Купить"
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(4):
        with open(f'{products[i][2]}', 'rb') as img:
            await message.answer_photo(img,
                f'Название: {products[i][0]} ' +
                f'| Описание: {products[i][1]} ' +
                f'| Цена: {(i + 1) * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_buy)


# Обработка нажатия инлайн-кнопки с продуктом
@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


# Объявляю класс состояний
class UserState(StatesGroup):
    # Состояние "Возраст"
    age = State()
    # Состояние "Рост"
    growth = State()
    # Состояние "Вес"
    weight = State()


# Обработка нажатия инлайн-кнопки "Рассчитать норму калорий"
@dp.callback_query_handler(text='calories')
async def set_age(call):
    # Запрос возраста у пользователя
    await call.message.answer('Введите свой возраст (целое число) в годах:')
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
        answer_text: str = ('Вам необходимо килокалорий (ккал) в сутки:\n' +
                            str(male_gender) + ' (для мужчин)\n' +
                            str(female_gender) + ' (для женщин)')
        # Отправляю пользователю текст с рассчитанным значением калорий
        await message.answer(answer_text)
        # Закрываю машину состояний
        await state.finish()
    else:
        await message.answer('Неверное значение. Введите свой вес в килограммах:')


# Обработка нажатия инлайн-кнопки "Формула расчёта"
@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    info_text: str = ('Формула Миффлина-Сан Жеора\nдля мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + '
                      '5\nдля женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.message.answer(info_text)
    await call.answer()


# Обработка всех остальных сообщений и команд
@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
