# Задача "План перехват"
def personal_sum(numbers):
#    print('1 TYPE of numbers:', type(numbers))
    result : int = 0
    incorrect_data : int = 0
# Внешний блок исключений для обработки ошибок с коллекцией numbers
    try:
# Перебор элементов коллекции numbers
        for n in numbers:
# Внутренний блок исключений для обработки ошибок с каждым элементом коллекции
            try:
# Суммирую каждый элемент коллекции в общий итог
                result += n
            except TypeError:
# Если при операции суммирования возникает исключение TypeError - обновляю счётчик ошибок
                print(f'Некорректный тип данных для подсчёта суммы - {n}')
                incorrect_data += 1
    except TypeError:
        print('В numbers записан некорректный тип данных')
    return (result, incorrect_data)

def calculate_average(numbers):
    personal_sum_tuple = personal_sum(numbers)
    try:
# Рассчёт среднего арифметического с учётом некорректных элементов коллекции numbers
        return personal_sum_tuple[0] / (len(numbers) - personal_sum_tuple[1])
    except TypeError:
        return None
    except ZeroDivisionError:
        return 0

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
