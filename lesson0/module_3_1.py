def count_calls():
# Использую глобальную переменную calls
    global calls
# Инкремент счётчика вызова функции
    calls += 1

def string_info(string):
# Вызываю функцию счётчика
    count_calls()
# Создаю и заполняю кортеж
    tuple_out = [len(string), string.upper(), string.lower()]
    return tuple_out

def is_contains(string, list_to_search):
# Вызываю функцию счётчика
    count_calls()
# Создаю новый список с элементами в верхнем регистре
    list_to_search_upper = [x.upper() for x in list_to_search]
# Сравниваю строку в верхнем регистре со списком элементов в верхнем регистре
    if string.upper() in list_to_search_upper:
        return True
    else:
        return False

# Обнуляю счётчик вызова функций
calls = 0


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)