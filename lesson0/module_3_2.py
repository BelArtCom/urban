def find_at(address, at = '@'):
# Функция проверяет наличие символа @ в адресе
    status = False
    if address.find(at) > 0:
        status = Truedef find_at(address, at = '@'):
# Функция проверяет наличие символа @ в адресе
    status = False
    if address.find(at) > 0:
        status = True
    return status

def find_domen(address, domens):
# Функция определяет, что адрес входит в разрешённый домен (по окончанию адреса)
    status = False
    for x in domens:
        if address.endswith(x):
            status = True
            break
    return status

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
# Основная функция производит сравнение адресатов с условиями задачи и выводит на экран соответствующее сообщение
# Разрешённые домены для адресатов поместил в список domens
    domens = ['.com', '.ru', '.net']
#    Отчёт по статусам функций для адресатов
#    print('Сообщение:                             ', message)
#    print('Получатель:                            ', recipient)
#    print('Получатель (наличие @):                ', find_at(recipient))
#    print('Получатель (принадлежность домену):    ', find_domen(recipient, domens))
#    print('Отправитель:                           ', sender)
#    print('Отправитель (наличие @):               ', find_at(sender))
#    print('Отправитель (принадлежность домену):   ', find_domen(sender, domens))

    if not find_at(recipient) or not find_at(sender) or not find_domen(recipient, domens) or not find_domen(sender, domens):
#       Если хоть один из адресатов (отправитель, получатель) не удовлетворяет заданным условиям, отправка сообщения считается невозможной
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
#       Проверка на равенство адресов отправителя и получателя
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
#       Проверка на использование адреса отправителя по умолчанию
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
#       В остальных случаях отправка сообщения происходит c нестандартного адреса
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
    return status

def find_domen(address, domens):
# Функция определяет, что адрес входит в разрешённый домен (по окончанию адреса)
    status = False
    for x in domens:
        if address.endswith(x):
            status = True
            break
    return status

def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
# Основная функция производит сравнение адресатов с условиями задачи и выводит на экран соответствующее сообщение
# Разрешённые домены для адресатов поместил в список domens
    domens = ['.com', '.ru', '.net']
#    Отчёт по статусам функций для адресатов
#    print('Сообщение:                             ', message)
#    print('Получатель:                            ', recipient)
#    print('Получатель (наличие @):                ', find_at(recipient))
#    print('Получатель (принадлежность домену):    ', find_domen(recipient, domens))
#    print('Отправитель:                           ', sender)
#    print('Отправитель (наличие @):               ', find_at(sender))
#    print('Отправитель (принадлежность домену):   ', find_domen(sender, domens))

    if not find_at(recipient) or not find_at(sender) or not find_domen(recipient, domens) or not find_domen(sender, domens):
#       Если хоть один из адресатов (отправитель, получатель) не удовлетворяет заданным условиям, отправка сообщения считается невозможной
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif sender == recipient:
#       Проверка на равенство адресов отправителя и получателя
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
#       Проверка на использование адреса отправителя по умолчанию
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
#       В остальных случаях отправка сообщения происходит от нестандартного отправителя
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
