# print('Привет, ' + 'мир!')
# print('Меня зовут %(name)s, мне %(year)s' % {'name': 'Тамерлан', 'year': 14})
# print('Я учусь в {title}{postfix} {title}'.format(title='Урбан', postfix='-university'))
# print(f'{"Urban" * 2} это лучший университет')


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4
challenge_result = ()

if score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('%(text)s %(team_num1)d %(!)s' % {'text': 'В команде Мастера кода участников: ', 'team_num1':5, '!':str('!')})
print('%(text)s %(team_num1)d %(и)s %(team_num2)d %(!)s' % {'text': 'Итого сегодня в команде участников: ',
                                                            'team_num1':5, 'и':'и', 'team_num2':6, '!':str('!')})
print('Команда Волшебники решили данных решили задач: {score_2}'.format(score_2=42))
print('Волшебники данных решили задачи на {team1_time} с!'.format(team1_time=18015.2))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')