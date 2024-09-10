# Родительский класс Horse, описывающий лошадь
class Horse:
    def __init__(self):
        print('INIT HORSE')
        self.x_distance = 0 # пройденный путь
        self.sound = 'Frrr' #звук, который издаёт лошадь

# Метод run изменяет дистанцию на dx
    def run(self, dx):
        self.x_distance += dx

# Родительский класс Eagle, описывающий орла
class Eagle:
    def __init__(self):
        print('INIT EAGLE')
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл (отсылка)

# Метод fly изменяет высоту полёта на dy
    def fly(self, dy):
        self.y_distance += dy

# Дочерний класс Pegasus, описывающий пегаса, наследуется от Horse и Eagle
class Pegasus(Horse, Eagle):
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования
    def __init__(self):
        print('INIT PEGASUS')
        self.x_distance = Horse().x_distance
        self.y_distance = Eagle().y_distance
        self.sound = Horse().sound
        self.sound = Eagle().sound

# Метод move вызывает методы run и fly родительских классов
    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy
        super().run(self.dx)
        super().fly(self.dy)

# Метод get_pos возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

# Метод voice печатает значение унаследованного атрибута sound
    def voice(self):
        print(self.sound)

print('Цепочка наследования MRO ----------------------------------------------')
print('Класс   Horse: ', Horse.mro())
print('Класс   Eagle: ', Eagle.mro())
print('Класс Pegasus: ', Pegasus.mro())
print('-----------------------------------------------------------------------')

print('Создание экземпляра класса Pegasus')
p1 = Pegasus()
print('Результат -------------------------------------------------------------')
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
