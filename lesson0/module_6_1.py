class Animal:
    alive = True # Живой
    fed = False # Накормленный
    def __init__(self, name):
        self.name = name # Индивидуальное название каждого животного

    def eat(self, food):
#        self.food = food
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False



class Plant:
    edible = False # Съедобность
    def __init__(self, name):
        self.name = name # Индивидуальное название каждого растения


class Mammal(Animal):
    pass
class Predator(Animal):
    pass

class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
