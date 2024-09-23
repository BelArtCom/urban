# Задание "Программистам всё можно"
def add_everything_up(a, b):
# Выполняю сложение параметров
    try:
        return a + b
# При возникновении имключения TypeError складываю параметры как строки
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
