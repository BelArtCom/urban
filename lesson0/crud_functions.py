import sqlite3
import random


# Генератор 8-значного номера id
def gen_id():
    id: str = ''
    for i in range(1, 8):
        id += str(random.randint(1, 9))
    return int(id)


def create_db():
    # Подключение к БД
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    # Создание таблицы Products
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image TEXT NOT NULL
    );
                   ''')

    # Создание таблицы Users
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
                   ''')

    # Проверка заполненности таблицы
    cursor.execute('SELECT count(*) FROM Products')
    total_products = cursor.fetchone()[0]

    # Отключение от БД
    connection.commit()
    connection.close()

    return total_products


def insert_data():
    # Подключение к БД
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    # Заполнение таблицы Products данными
    for i in range(4):
        products = [
            ['Витамин C', 'Антиоксидант', 'Vit_C.webp'],
            ['Витамин D3', 'Обмен кальция и фосфора', 'Vit_D.webp'],
            ['Витамин E', 'Замедляет старение клеток', 'Vit_E.webp'],
            ['Витамин Омега-3', 'Здоровье сердца и сосудов', 'Vit_Omega.webp']
        ]
        cursor.execute(f"INSERT INTO Products (id, title, description, price, image) VALUES ({gen_id()},"
                       f"'{products[i][0]}', '{products[i][1]}', {(i + 1) * 100}, '{products[i][2]}')")

    # Отключение от БД
    connection.commit()
    connection.close()


def initiate_db():
    create_db()
    # Если таблица Products пуста, заполняем её данными
    if not create_db():
        insert_data()


def get_all_products():
    # Создание и заполнение БД
    initiate_db()

    # Подключение к БД
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    # Выборка данных из таблицы Products
    cursor.execute('SELECT * FROM Products ORDER BY id')
    products = cursor.fetchall()

    # Отключение от БД
    connection.commit()
    connection.close()

    return products


def add_user(username, email, age):
    # Подключение к БД
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES ('{username}', '{email}', '{age}', 1000)")
    connection.commit()
    connection.close()


def is_included(username):
    # Подключение к БД
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM Users WHERE username = '{username}'")
    user = cursor.fetchone()[0]
    connection.commit()
    connection.close()
    # Использую неявное преобразование в булевы 'Истина' или 'Ложь' при наличии username в таблице
    return user
