# Задача "Записать и запомнить"
from pprint import pprint

def custom_write(file_name, strings):
# Создаю переменную для хранения номера строки (счётчик строк)
    i = 1
# Создаю пустой словарь для добавления результата выполнения функции
    strings_positions = dict()
# Открываю файл, имя файла передано параметром при вызове функции
    file = open(file_name, 'a', encoding='utf-8')
# Циклом перебираю переданный при вызове функции список строк
    for s in strings:
# Формирую новую запись в словаре с участием текущей строки по условию задачи
        strings_positions[(i, file.tell())] = s
# Записываю текущую строку в файл с символом переноса каретки
        file.write(s + '\n')
# Инкрементом обновляю счётчик строк для следующей итерации цикла
        i += 1
# После выхода из цикла закрываю файл
    file.close()
# Функция возвращает сформированный в цикле словарь
    return strings_positions

# Выполнение
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
