import sqlite3

# Задача "Первые пользователи"

# Подключение к БД
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# Создание таблицы Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
               ''')

# Заполнение таблицы Users данными
for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', i * 10,  1000))

# Обновление balance у каждой 2ой записи начиная с 1ой
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = 500 WHERE username = ?', (f'User{i}',))

# Удаление каждой 3ей записи в таблице начиная с 1ой:
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))

# Запрос для выборки данных из таблицы Users
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()

# Вывод на экран значений из таблицы в формате: "Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>"
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удаление всех данных в таблице Users
#cursor.execute('DELETE FROM Users WHERE username like ?', ('User%', ))

# Коммит и закрытие соединения
connection.commit()
connection.close()