def get_multiplied_digits(number):
# Перевожу полученное число в строку
    str_number = str(number)
# переменной first присваиваю значение первого символа (цифры) полученного числа
    first = int(str_number[0])
# Если длина строки str_number более 1 символа, функция возвращает произведение первого символа (числа) строки str_number из "прошлого" запуска функции в рекурсии с первым символом строки из текущего запуска
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
# Иначе функция возвращает первый (единственный) символ (число)
    else:
        return first

result = get_multiplied_digits(40203)
print(result)