# Задача "Вызов разом"
def apply_all_func(int_list, *functions):
# Создаю пустой словарь для внесения результатов
    results = dict()
# Циклом прохожу по скиску переданных функций
    for func in functions:
# Вношу запись в словарь (ключ - имя функции: значение - результат выполнения функции)
        results[func.__name__] = func(int_list)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))