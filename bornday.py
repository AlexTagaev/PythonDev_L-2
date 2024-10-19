born_year = int(input('Введите год рождения А.С.Пушкина: '))
if born_year == 1799:
    day_born = input('Введите дату рождения А.С.Пушкина (в формате dd.mm): ')
    if day_born == '06.06':
        print('Верно!')
    else:
        print('Неверный день рождения...')
else:
    print('Неверный год рождения...')