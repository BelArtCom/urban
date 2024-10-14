# Задача "Многопроцессное считывание"

import datetime, multiprocessing

filenames = [f'file {number}.txt' for number in range(1, 5)] # Список файлов

def read_info(name): # Функция открывает файл с переданным именем и записывает все строки из него в список all_data
    all_data = [] # Пустой список для добавления строк из файлов
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.rstrip())

# ЛИНЕЙНЫЙ ВЫЗОВ
print('Линейный вызов')
start = datetime.datetime.now() # Засечка времени
for file_name in filenames: # В цикле для каждого файла в списке filenames запускаю функцию read_info
    read_info(file_name)
finish = datetime.datetime.now() # Засечка времени
time_result = (finish - start).total_seconds() # Вычисление потраченного времени в секундах
print(f'Потрачено времени: {time_result} сек')

# МНОГОПРОЦЕССОРНЫЙ ВЫЗОВ
#if __name__ == '__main__':
#    print('Многопроцессорный вызов')
#    start = datetime.datetime.now() # Засечка времени
#    with multiprocessing.Pool(processes=4) as pool:
#        pool.map(read_info, filenames) # Выполняю функцию read_info в многопроцессорном режиме для каждого файла из списка filenames
#    finish = datetime.datetime.now() # Засечка времени
#    time_result = (finish - start).total_seconds() # Вычисление потраченного времени в секундах
#    print(f'Потрачено времени: {time_result} сек')
