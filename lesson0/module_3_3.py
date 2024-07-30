def print_params(a = 1, b = 'строка', c = True):
    print('a =', a, '   b =', b, '   c =', c)
#    print('b =', b)
#    print('c =', c)

print_params(b = 25)
print_params(c = [1,2,3])
# вызов функции с 4-мя параметрами закончился ошибкой
#print_params(1, 2, 3, 4)

values_list = [True, "Два", 3]
values_dict = {'a': 1, 'b': 2, 'c': 3}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)