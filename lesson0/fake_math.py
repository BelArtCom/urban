def divide(first, second):
# Использую неявное преобразование аргумента second в булев тип (0 - False, все остальные значения - True)
    if second:
        return first / second
    else:
        return 'Ошибка'
