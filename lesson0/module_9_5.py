# Задача "Range - это просто"
class StepValueError(ValueError):
    pass
class Iterator:
    def __init__(self, start : int, stop : int, step = 1):
        self.start = start              # целое число с которого начинается итерация
        self.stop = stop                # целое число на котором заканчивается итерация
        self.pointer = self.start       # текущее число в итерации
# Проверка на нулевой шаг
        if step == 0:
            raise StepValueError()
        else:
            self.step = step            # шаг с которым совершается итерация
    def __iter__(self):
# Так как метод __next__ выдаёт следующий элемент итерации, первый элемент теряется
# Поэтому делаю "шаг назад", чтобы получить корректный список элементов с первого до последнего
        self.pointer = self.start - self.step
        return self
    def __next__(self):
        self.pointer += self.step
# Управление поведением итератора в зависимости от шага (+/-) и достижения последнего элемента
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration()
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()