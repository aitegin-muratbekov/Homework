from random import randint

def akinator(min_number, max_number):
    result = max_number//2
    print(f'ПРЕДСКАЗЫВАЮ вы выбрали число от {min_number} до {max_number}')

    while True:
        print(result)
        answer = input('Это ваше число?')

        if answer == 'да':
            with open('results.txt', 'r', encoding ='UTF-8') as file:
                lst = len(file.readlines()) + 1
            with open('results.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{result} {answer}\n')
                file.write(f'попыток : {lst}  число: {result}\n')
            print('Я прочитал твои мысли.До нового предсказания!')
            break
        elif answer == '>':
            with open('results.txt', 'a') as file:
                file.write(f'{result} {answer}\n')
            min_number = result + 1
            result = (min_number + max_number)//2
        elif answer == '<':
            with open('results.txt', 'a') as file:
                file.write(f'{result} {answer}\n')
            max_number = result - 1
            result = (min_number + max_number) //2
        else:
            print('ты должен написать ">" "<" или "да"!')

akinator(1, 100)


