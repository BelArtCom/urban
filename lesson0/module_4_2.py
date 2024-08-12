def test_function():
    print('START test_function')
    def inner_function():
        print('START inner_function')
        print('Я в области видимости функции test_function')
    inner_function()
#inner_function()
# При вызове внутренней функции inner_function вне функции test_function выходит ошибка
# name 'inner_function' is not defined
# Система не видит определения функции
# Python не понимает, откуда взялась функция inner_function и не знает, как с ней работать
# Функция inner_function находится вне области видимости

test_function()