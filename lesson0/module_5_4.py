class House():
    houses_history = []

    def __new__(cls, *args):
        # Методом append добавляю в список cls.houses_history наименование созданного жилищного комплекса
        # Наименование получаю из переданного кортежа аргументов (аргумент name под индексом 0)
        cls.houses_history.append(args[0])
        # Чтобы объект класса создался, необходимо, чтобы метод __new__ вернул объект
        # Добиваюсь этого, используя метод __new__ родительского класса object
        return super().__new__(cls)
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)





