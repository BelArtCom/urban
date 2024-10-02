# Задача "За честь и отвагу!"
from threading import Thread
from time import sleep

class Knight(Thread):
    num_enemies : int = 100 # Число врагов
    days: int = 0 # Счётчик дней

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(self.name + ', на нас напали!')
        while self.num_enemies > 0:
            self.days += 1 # Счётчик дней
            self.num_enemies -= self.power # Рассчёт числа оставшихся врагов
            print(f'{self.name} сражается {self.days} день(дня)..., осталось {self.num_enemies} воинов.')
            sleep(1)  # Длительность одного дня
        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Остановка потоков
first_knight.join()
second_knight.join()

print('Все битвы закончились!')