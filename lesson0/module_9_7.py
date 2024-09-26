# Задание: Декораторы в Python
def is_prime(func):
    def wripper(*arg):
        result = func(*arg)
        prime_count : int = 0
# Проверка на простое число
        for i in range(result):
            if i > 1 and i < result and result % 2 == 0:
                prime_count += 1
        if prime_count > 0:
            print('Составное')
        else:
            print('Простое')
        return result
    return wripper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
