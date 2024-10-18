born_year = int(input('Введите год рождения А.С.Пушкина: '))
if born_year == 1799:
    day_born = input('Введите дату рождения А.С.Пушкина: ')
    if day_born == '6 июня':
        print('Верно!')
    else:
        print('Неверный день рождения...')
else:
    print('Неверный год рождения...')