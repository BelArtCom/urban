def get_matrix(n, m, value):
    # Создаю пустой список matrix
    matrix = []
    for i in range(n):
        # Добавляю новый элемент в список (новый элемент является пустым списком)
        matrix.append([])
        for j in range(m):
            # В списке matrix присваиваю значение value j-тому элементу i-го списка
            matrix[i].insert(j, value)
    # Функция возвращает заполненный список matrix, состоящий из списков
    return matrix

# Присваиваю переменным result1, result2, result3 списки через вызов функции get_matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
# Вывожу результат на экран
print(result1)
print(result2)
print(result3)