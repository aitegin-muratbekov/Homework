ten = list(range(1, 11))
evens = list(filter(lambda x: x % 2 == 0, ten))
second_power = list(map(lambda x: x*x, evens))
print(second_power)

def find_object(a = []):
    while True:
        index = input()
        if index != 'quit' :
            try:
                print(a[int(index)])
                continue
            except IndexError:
                print('Введите правильный индекс')
                continue
            except ValueError:
                print('Введите число или "quit" ')
        break
    return print('Программа завершена')

print(find_object(a = ten))








