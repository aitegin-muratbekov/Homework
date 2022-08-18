english = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
russian = 'йцукенгшщзхъфывапролджэячсмитьбю'



finish = False

while finish == False:
    word = input("\n Введите слово  ").lower()
    for i in word:
        if i == 'q' or i == 'й':
            print("Программа завершена")
            finish = True
        elif i in english:
                print(russian[english.index(i)], end='')
        elif i in russian:
                print(english[russian.index(i)], end='')
        else:
            print("не правильно!")
            break




