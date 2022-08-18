date = input('Введите дату и месяц вашего рождения: ')

date_of_birth = int(date[:2])
month_of_birth = date[-2:]

if 20 < date_of_birth < 32 and month_of_birth == '03' or 0 < date_of_birth < 20 and month_of_birth == '04':
    print('Ваш знак зодиака : Овен')

elif 20 < date_of_birth < 31 and month_of_birth == '04' or 0 < date_of_birth < 21 and month_of_birth == '05':
    print('Ваш знак зодиака : Телец')

elif 20 < date_of_birth < 32 and month_of_birth == '05' or 0 < date_of_birth < 21 and month_of_birth == '06':
    print('Ваш знак зодиака : Близнецы')

elif 20 < date_of_birth < 31 and month_of_birth == '06' or 0 < date_of_birth < 23 and month_of_birth == '07':
    print('Ваш знак зодиака : Рак')

elif 22 < date_of_birth < 32 and month_of_birth == '07' or 0 < date_of_birth < 23 and month_of_birth == '08':
    print('Ваш знак зодиака : Лев')

elif 22 < date_of_birth < 32 and month_of_birth == '08' or 0 < date_of_birth < 23 and month_of_birth == '09':
    print('Ваш знак зодиака : Дева')

elif 22 < date_of_birth < 31 and month_of_birth == '09' or 0 < date_of_birth < 23 and month_of_birth == '10':
    print('Ваш знак зодиака : Весы')

elif 22 < date_of_birth < 32 and month_of_birth == '10' or 0 < date_of_birth < 22 and month_of_birth == '11':
    print('Ваш знак зодиака : Скорпион')

elif 22 < date_of_birth < 31 and month_of_birth == '11' or 0 < date_of_birth < 23 and month_of_birth == '12':
    print('Ваш знак зодиака : Стрелец')

elif 22 < date_of_birth < 32 and month_of_birth == '12' or 0 < date_of_birth < 21 and month_of_birth == '01':
    print('Ваш знак зодиака : Козерог')

elif 20 < date_of_birth < 32 and month_of_birth == '01' or 0 < date_of_birth < 20 and month_of_birth == '02':
    print('Ваш знак зодиака : Водолей')

elif 19 < date_of_birth < 30 and month_of_birth == '02' or 0 < date_of_birth < 21 and month_of_birth == '03':
    print('Ваш знак зодиака : Рыбы')