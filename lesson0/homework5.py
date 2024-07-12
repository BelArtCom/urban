# Создаю кортеж
immutable_var = (12, 34.5, True, 'String_value', [1, 2])
print('immutable_var type:', type(immutable_var))
print('Immutable tuple:', immutable_var)
print('Immutable tuple first element:', immutable_var[0])
# Пытаюсь изменить первый (с индексом 0) элемент кортежа
#immutable_var[0] = False
# Получаю ошибку:
# TypeError: 'tuple' object does not support item assignment
# Появление ошибки вызвано попыткой изменить "неизменяемый" тип данных (immutable), в данном случае int

# Кортеж является неизменяемым типом данных (immutable)
# Однако, элемент кортежа может быть изменяемыми, если его тип изменяемый (mutable)
# Например: список, словарь или множество (их содержимое можно изменить)
immutable_var[4][0] = 3
print('Immutable tuple:', immutable_var)

# Создаю список
mutable_list = [False, 'String_value', 67, 89.5, [6, 7]]
print('mutable_list type:', type(mutable_list))
print('Mutable list:', mutable_list)
# Редактирую список
mutable_list = [True, 'New_string_value', 'Old_string_value', 50, 60.5, [8, 9]]
print('Editing mutable list:', mutable_list)
# Методом append добавляю логическое значение False
mutable_list.append(False)
print('Editing mutable list:', mutable_list)
# Методом remove удаляю строковое значение "Old_string_value"
mutable_list.remove('Old_string_value')
print('Editing mutable list:', mutable_list)
