# Задача "Банковские операции"

import threading, random
#import random
from time import sleep

class Bank:
    def __init__(self):
        self.balance: int = 0              # Баланс банка
        self.lock: Lock = threading.Lock() # Объект класса Lock для блокировки потоков

    def deposit(self):
        for i in range(1, 100):
            deposit_pay = random.randint(50, 500) # Определение случайного числа для зачисления на счёт
            if self.balance >= 500 and self.lock.locked():
                print('Разблокировка')
                self.lock.release() # Разблокировка
            self.balance += deposit_pay
            print(f'Пополнение: {deposit_pay}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(1, 100):
            take_pay = random.randint(50, 500) # Определение случайного числа для снятия со счёта
            print(f'Запрос на {take_pay}')
            if take_pay <= self.balance:
                self.balance -= take_pay
                print(f'Снятие: {take_pay}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
