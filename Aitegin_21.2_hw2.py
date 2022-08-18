
day = input("Введите свой день рождения  ")

month = str(day[-2:])
day = int(day[0:2])


if month == '03' and 21 <= day <= 31 or  month == '04' and 1 <= day <= 20:
    print('Овен')
elif month == '04' and 21 <= day <= 30 or  month == '05' and 1 <= day <= 20:
    print('Телец')
elif month == '05' and 21 <= day <= 31 or  month == '06' and 1 <= day <= 20:
    print('Близнецы')
elif month == '06' and 21 <= day <= 30 or  month == '07' and 1 <= day <= 22:
    print('Рак')
elif month == '07' and 23 <= day <= 31 or  month == '08' and 1 <= day <= 22:
    print('Лев')
elif month == '08' and 23 <= day <= 30 or  month == '09' and 1 <= day <= 22:
    print('Дева')
elif month == '09' and 23 <= day <= 31 or  month == '10' and 1 <= day <= 22:
    print('Весы')
elif month == '10' and 23 <= day <= 30 or  month == '11' and 1 <= day <= 22:
    print('Скорпион')
elif month == '11' and 23 <= day <= 31 or  month == '12' and 1 <= day <= 21:
    print('Стрелец')
elif month == '12' and 22 <= day <= 30 or  month == '01' and 1 <= day <= 19:
    print('Козерог')
elif month == '01' and 20 <= day <= 31 or  month == '02' and 1 <= day <= 19:
    print('Водолей')
elif month == 2 and 20 <= day <= 28 or  month == 3 and 1 <= day <= 20:
    print('Рыбы')
