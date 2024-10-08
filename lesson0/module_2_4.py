# Белянский А.С.

# Создаю списки
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

# Основной цикл проходит по всем элементам списка
for i in numbers:
    if i == 1:
        continue # Число 1 не является ни простым, ни составным числом, его пропускаю
    else:
        is_prime = True # Создаю флаг простого числа
# Внутренний цикл проверяет остаток от деления элемента основного списка на все числа кроме 1 и самого элемента
# Если остаток от деления хоть на одной итерации внутреннего цикла будет равен нулю
# флаг простого числа реверсиуется и выполнение цикла прекращается
        for j in range(1, i):
            if j != 1 and j != i and i%j == 0:
                is_prime = False
                break
# Проверка флага на простое число
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)
