# Создаю словарь
my_dict = {'John': 1985, 'Alex': 1996, 'Elena': 1976, 'Simon': 1991}
print('my_dict type:', type(my_dict))
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Simon'))
print('Not existing value:', my_dict.get('Dimon'))
# Можно использовать второй вариант
print(my_dict.get('Dimon', 'Not existing value:'), 'Dimon')

# Добавляю две произвольные пары в словарь
my_dict.update({'Max': 1990, 'Nikita': 1989})
# Метод словаря pop позволяет удалить из словаря пару Ключ:Значение
# Но вывести на экран удалённое значение пары или сохнанить его в переменную
print('Deleted value:', my_dict.pop('John'))
print('Modified dictionary:', my_dict)

# Создаю множество
my_set = {1, 2, 3, 3, 7, 3, 5.5, 5.5, 'String', 'New_String', 'Old_String', 'String', True, True, False, False}
print('my_set type:', type(my_set))
print('Set:', my_set)
# Добавляю два новых значения в множество
my_set.update([8, 9])
# Удаляю одно значение из множества
my_set.remove(3)
print('Modified set:', my_set)

# Проверяю наличие логических значений True и False в множестве
#print('True in my_set:', True in my_set)
#print('False in my_set:', False in my_set)

# Перебор всех элементов множества подтверждает наличие False, но наличие True не подтверждается
#for num in my_set:
#   print('my_set element:', num)
