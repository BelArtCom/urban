# Задача "Потоковая запись в файлы"

from threading import Thread
from time import sleep
from datetime import datetime
def write_words(word_count, file_name):
    file = open(file_name, 'w+', encoding='utf-8')
    for word in range(1, word_count + 1):
        file.write(f'Какое-то слово № {word}\n')
        sleep(0.1)
    print(f'Завершилась запись в файл {file.name}')
    file.close()

# Тест записи в 1 поток
print('Запись в 1 поток:')
time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_finish = datetime.now()
time_result_1 = time_finish - time_start
print(f'Затрачено времени -', time_result_1.total_seconds(), 'сек')
print('--------------------------------------')

# Тест записи в 4 потока
print('Запись в 4 потока:')
time_start = datetime.now()

thread_01 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_02 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_03 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_04 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_01.start()
thread_02.start()
thread_03.start()
thread_04.start()

thread_01.join()
thread_02.join()
thread_03.join()
thread_04.join()

time_finish = datetime.now()
time_result_2 = time_finish - time_start
print(f'Затрачено времени -', time_result_2.total_seconds(), 'сек')
print('--------------------------------------')
print(f'Многопотоковая запись быстрее на', (time_result_1 - time_result_2).total_seconds(), 'сек')

