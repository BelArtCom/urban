# Домашнее задание по теме "Форматирование строк"

# Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

#tasks_total = score_1 + score_2
#time_avg = (team1_time + team2_time) / tasks_total


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


#if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:result = 'Победа команды Мастера кода!'
#elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:result = 'Победа команды Волшебники Данных!'
#else:result = 'Ничья!'
# Использование %:
#-----------------
# Количество участников первой команды
print('В команде Мастера кода участников: %d ! ' % team1_num)

# Количество участников в обеих командах
print('Итого сегодня в командах участников: %(sum1)d и %(sum2)d !' % {'sum1': team1_num, 'sum2': team2_num})


# Использование format():
#------------------------
# Количество задач решённых командой 2
print('Команда Волшебники данных решила задач: {} !'.format(score_2))

# Время за которое команда 2 решила задачи
print('Волшебники данных решили задачи за {time} с ! '.format(time = team1_time))


# Использование f-строк:
#-----------------------

# Количество решённых задач по командам
print(f'Команды решили {score_1} и {score_2} задач.')

# Исход соревнования
print(f'Результат битвы: {challenge_result}')

# Количество задач и среднее время решения
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!.')

