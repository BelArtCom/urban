# Создаю класс House
class House():
# Настраиваю инициализатор для класса House
    def __init__(self, name, number_of_floors ):
# При инициализации класса House определяются атрибуты
# name (наименование жилищного комплекса) и
# number_of_floors (число этажей в доме)
        self.name = name
        self.number_of_floors = number_of_floors

# Создаю метод go_to класса House
    def go_to(self, new_floor):
# Если число этажей, переданное методом, не удовлетворяет нашим условиям, выводится сообщение
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
# Иначе происходит обработка данных
        else:
# Вывод всех этажей от 1 до переданного методом
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
