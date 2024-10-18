import requests, numpy as np, pandas as pd, matplotlib, datetime

'''
ДЕМОНСТРАЦИЯ ПРИМИМНЕНИЯ БИБЛИОТЕКИ requests
Скрипт проверяет по ИНН наличие организации в Реестре участников бюджетного процесса, а также юридических лиц,
не являющихся участниками бюджетного процесса
https://www.budget.gov.ru/Бюджет/Расходы/Реестр-участников-и-неучастников-бюджетного-процесса
Структура JSON-документа описана на странице API: https://www.budget.gov.ru/Открытые-данные?code=7710568760-RUBPNUBP

Пользователь вводит искомый ИНН через input
Можно искать не полный ИНН, а только комбинацию нескольких цифр, например 12345
поиск осуществляется в режиме фильтра (параметр запроса filterinn=inn)
Порталом ограничего количество возвращаемых записей (999 штук, параметр запроса pageSize)
Результат выводится в консоль
Отчёт также выводится в файл 'inn_report.txt'
'''

def print_report(line): # Функция формирует отчёт report для записи в файл
    global report
    print(line)
    report += line + '\n'

def write_report(time_stamp: str): # Функция записывает итоговый отчёт report в файл
    global report
    report_filename: str = 'inn_report.txt'
    file = open(report_filename, 'a', encoding='utf-8')
    report += 'Время составления отчёта:   ' + time_stamp
    report += '----------------------------------------------------------' + '\n'
    file.write(report)
    file.close()

inn = input('Введите ИНН (примеры: 2700000786, 2700000176, 2722033182, 1689545898, 12345) для поиска организации: ')
count_find: int = 0
count_report: int = 0
report: str = ''
print_report(f'Поиск по фильтру ИНН {inn}')

# Портал электронного бюджета в ответ на запрос формирует JSON-документ с данными организаций
# Метод requests.get посылает get-запрос на указанный адрес
# Метод response.json() возвращает закодированное в json содержимое ответа в виде словаря

try:
    response = requests.get(f'http://budget.gov.ru/epbs/registry/ubpandnubp/data?filterinn={inn}&pageSize=999')
    full_info: dict = dict(response.json())
except:
    print('Запрос не может быть выполнен')

# Поле recordCount указывает число записей по указанному фильтру ИНН
# Если фильтр не найдёт по введённому ИНН ни одной записи, в поле recordCount будет 0
# Атрибут response.status_code - целочисленный код ответа HTTP-статуса, например 404 или 200
# Атрибут response.reason - текстовое представление ответа HTTP-статуса, например 'Not Found' или 'OK'

if response.status_code == requests.codes.ok: # Проверка возвращаемого HTTP-статуса
    if full_info['recordCount'] > 0: # Проверка наличия данных в ответе от сервера
        count_find = full_info['recordCount']
        for data_dict in full_info['data']:
            count_report += 1
            info_dict: dict = dict(data_dict['info'])

            innNumber: str = info_dict['inn'] # ИНН
            fullName: str = info_dict['fullName'] # Полное наименование организации
            shortName: str = info_dict['shortName'] # Сокращенное наименование организации
            orgTypeName: str = info_dict['orgTypeName'] # Наименование типа организации
            statusName: str = info_dict['statusName'] # Наименование статуса организации
            postIndex: str = info_dict['postIndex'] # Почтовый индекс организации
            cityType: str = info_dict['cityType'] # Тип населённого пункта
            cityName: str = info_dict['cityName'] # Наименование населённого пункта
            streetType: str = info_dict['streetType'] # Тип улицы
            streetName: str = info_dict['streetName'] # Наименование улицы
            house: str = info_dict['house'] # Дом

            print_report('ОРГАНИЗАЦИЯ')
            print_report(f'ИНН:                        {innNumber}')
            print_report(f'Полное наименование:        {fullName}')
            print_report(f'Сокращенное наименование:   {shortName}')
            print_report(f'Тип организации:            {orgTypeName}')
            print_report(f'Статус:                     {statusName}')
            print_report(f'Адрес:                      {postIndex}, {cityType} {cityName}, {streetType} {streetName}, {house}')

            for contacts_dict in data_dict['contacts']:
                phone: str = contacts_dict['phone'] # Телефонный номер
                site: str = contacts_dict['site'] # Сайт
                mail: str = contacts_dict['mail'] # Адрес электронной почты

                print_report('КОНТАКТЫ')
                print_report(f'Телефонный номер:           {phone}')
                print_report(f'Сайт:                       {site}')
                print_report(f'Адрес электронной почты:    {mail}')

            for heads_dict in data_dict['heads']:
                fio: str = heads_dict['fio'] # ФИО руководителя
                post: str = heads_dict['post'] # Должность руководителя

                print_report('РУКОВОДИТЕЛЬ')
                print_report(f'ФИО:                        {fio}')
                print_report(f'Должность:                  {post}')
            print_report('----------------------------------------------------------')
    else:
        print_report(f'ИНН {inn} НЕ НАЙДЕН')
        print_report('----------------------------------------------------------')

    if count_find > count_report:
        print_report('Для более точного поиска в ИНН должно быть больше символов')

    print_report('Найдено совпадений:         ' + str(count_find))
    print_report('Обработано записей:         ' + str(count_report))
    write_report(str(datetime.datetime.now()) + '\n') # Запись сформированного отчёта в файл с временной меткой

else:
    print('Проблемы с соединением:', response.reason)
