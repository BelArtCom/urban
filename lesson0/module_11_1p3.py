import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import urllib.request
from xml.dom import minidom
from io import StringIO

'''
ДЕМОНСТРАЦИЯ ПРИМИМНЕНИЯ БИБЛИОТЕК pandas и matplotlib
Скрипт получает информацию о курсе выбранной валюты за указанный период 
с сайта Центрального Банка России (https://cbr.ru/)
На странице https://cbr.ru/development/SXML/ указана информация, какой запрос нужно сформировать для получения данных
Нужно указать 3 параметра:
 - дата начала периода
 - дата окончания периода
 - идентификатор валюты
Для примера взята валюта "Доллар США", USD, идентификатор R01235
Для безошибочной идентификации валюты используется Идентификатор валюты из справочника валют,
опубликованного на странице https://cbr.ru/scripts/XML_valFull.asp
Также скрипт получает информацию о наименовании валюты и номинале из того же справочника валют
Скрипт получает информацию и формирует XML-документ с курсами валюты за указанный период
Методами библиотеки pandas определяется минимальное, среднее и максимальное значение курса
Используя библиотеку matplotlib, вывожу 2 графика: с динамикой курса за период и со статистическими показателями
'''

currency_id: str = 'R01235' # Идентификатор валюты "Доллар США", USD
cur_label: str # Наименование валюты, определённое по Идентификатору
cur_label_name: str # Имя валюты
cur_label_nominal: str # Номинал валюты
date_start: str = '01/02/2020' # Начало периода
date_end: str = '31/12/2020' # Конец периода

# Адрес справочника валют
xml_cur_url: str = 'https://cbr.ru/scripts/XML_val.asp'
# Адрес запроса данных о курсах валюты
xml_url: str = f'https://cbr.ru/scripts/XML_dynamic.asp?date_req1={date_start}&date_req2={date_end}&VAL_NM_RQ={currency_id}'

currency_date: str # Дата валютного курса
currency_value: float = 0 # Значение валютного курса
currency_dict: dict = {} # Словарь для хранения информации о валютном курсе
currency_min: float # Минимальное значение валютного курса
currency_mean: float # Среднее значение валютного курса
currency_max: float # Максимальное значение валютного курса
currency_max_min: dict = {} # Словарь для хранения статистических показателей

# Получаю объект xml_file, содержащий xml-документ
xml_file = urllib.request.urlopen(xml_url)

# Считываю файл
main_data = xml_file.read()

# Метод parseString помогает распарсить документ main_data и помещает все данные в новый объект dom
dom = minidom.parseString(main_data)

# В объект-коллекцию elements загружаются все таги с именем 'Record'
elements = dom.getElementsByTagName('Record')

# Циклом прохожу по всем элементам распарсенного xml-документа
for node in elements:
    for child in node.childNodes:
# В каждом тэге 'Record' считываю атрибут 'Date'
        date_xml = node.getAttribute('Date')
# Перевожу в формат даты
        date_format = dt.datetime.strptime(date_xml, "%d.%m.%Y")
# Меняю формат отображения даты на YYYY.MM.DD
        currency_date = str(date_format.strftime("%Y.%m.%d"))
# В подчинённых тэгах ищу тэг 'Value' (цена валюты) и его значение записываю в переменную currency_value
        if child.tagName == 'Value':
            currency_value = float(child.firstChild.data.replace(',', '.'))
# Заполняю словарь currency_dict парами {'Дата': 'Курс валюты'}
        currency_dict[currency_date] = currency_value

# Сохраняю XML-документ (справочник валют) в объект xml_cur
xml_cur = urllib.request.urlopen(xml_cur_url)

# Формирую ДатаФрэйм с данными справочника валют
df_cur = pd.read_xml(StringIO(xml_cur.read(99999).decode('windows-1251')))

# Методом pandas.DataFrame преобразую полученный словарь currency_dict в ДатаФрэйм
df = pd.DataFrame(list(currency_dict.items()), columns=['Date', 'Value'])

# Нахожу значения минимального, среднего и максимального курса за выбранный период
currency_min = round(df['Value'].min(), 4)
currency_mean = round(df['Value'].mean(), 4)
currency_max = round(df['Value'].max(), 4)

# Вывод статистической информации (минимальное, среднее, максимальное значение за выбранный период)
print('Минимальное значение курса за период:  ', currency_min)
print('Среднее значение курса за период:      ', currency_mean)
print('Максимальное значение курса за период: ', currency_max)

# Создаю словарь currency_max_min с минимальным, средним и максимальным курсом
currency_max_min = {'Минимальное': currency_min, 'Среднее': currency_mean, 'Максимальное': currency_max}
# Создаю ДатаФрэйм df_stat из словаря
df_stat = pd.DataFrame(list(currency_max_min.items()), columns=['Stat', 'Value'])

print(df) # Вывод основной таблицы данных о курсах валюты

# Формирую данные о выбранной валюте
cur_label_name: str = df_cur['Name'].loc[df_cur['ID'] == currency_id].to_string(index=False, header=False)
cur_label_nominal: str = df_cur['Nominal'].loc[df_cur['ID'] == currency_id].to_string(index=False, header=False)
cur_label = f'{cur_label_name} ({cur_label_nominal} шт)'
print(f'Выбранная валюта: {cur_label}')

# Подготавливаю и показываю графики
plt.figure(figsize=(15, 7))
plt.subplot(1, 2, 1) # Задать область отображения графика
plt.plot(df['Date'], df['Value'], color='red', label=cur_label) # Задать данные для графика, цвет и наименование линии
plt.title('Изменение курса', pad=30, fontsize=15) # Задать заголовок графика
plt.xlabel('Дата', fontsize=15, color='blue') # Задать наименование оси X
plt.ylabel('Цена', fontsize=15, color='blue') # Задать наименование оси Y
plt.legend() # Рисовать легенду линии
plt.grid(False) # Не рисовать сетку
plt.subplot(1, 2, 2) # Задать область отображения графика
pl = plt.bar(df_stat['Stat'], round(df_stat['Value'], 4)) # Задать данные для графика
# Добавление подписей к колонкам графика
for bar in pl:
    plt.annotate(bar.get_height(), xy=(bar.get_x() + 0.15, bar.get_height() - 7), fontsize=15)
plt.xlabel('Показатель', fontsize=15, color='blue') # Задать наименование оси X
plt.show() # Показать график
