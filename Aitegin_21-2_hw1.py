tempCHUI = float(input("Введите температуру воздуха на сегодня в Чуе:"))
tempOSH = float(input("Введите температуру воздуха на сегодня в Оше:"))
tempNaryn = float(input("Введите температуру воздуха на сегодня в Нарыне:"))
tempTalas = float(input("Введите температуру воздуха на сегодня в Таласе:"))
tempDjalalAbad = float(input("Введите температуру воздуха на сегодня в Джалал-Абаде:"))
temopYssykKul = float(input("Введите температуру воздуха на сегодня в Ыссык-Куле:"))
tempBatken = float(input("Введите температуру воздуха на сегодня в Баткене:"))

sum_of_temp = tempCHUI + tempOSH + tempNaryn + tempTalas +\
            tempDjalalAbad + temopYssykKul + tempBatken
average_temp = round(sum_of_temp / 7, 1)

print(f'Средний показатель температуры воздуха по КР на сегодня {average_temp} °C')

#очень хочу 10 баллов)