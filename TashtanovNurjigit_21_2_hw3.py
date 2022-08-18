rus_alpha = 'йцукенгшщзхъфывапролджэячсмитьбю'
eng_alpha = "qwertyuiop[]asdfghjkl;'zxcvbnm,.'"

while True:
  word = input('\nДля выхода нажмите "q": ').lower()

  if word == 'q' or word == 'й' :
    break

  for i in word:
    result = ""
    if i in rus_alpha:
      counter = 0
      for f in rus_alpha:
        counter += 1
        if i == f:
          counter2 = 0
          for x in eng_alpha:
            counter2 += 1
            if counter == counter2:
              result += x;
              break
          break
    elif i in eng_alpha:
      counter = 0
      for f in eng_alpha:
        counter += 1
        if i == f:
          counter2 = 0
          for x in rus_alpha:
            counter2 += 1
            if counter == counter2:
              result += x;
              break
          break
    print(result, end='')