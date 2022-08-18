data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []
index = 0

for i in data_tuple :
    if type(i) == str :
        letters.append(i)
    else :
        numbers.append(i)

numbers.remove(6.13)
numbers.insert(1, 2)
numbers.sort()
letters.append(numbers.pop(0))
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'

for i in numbers:
    i = i ** 2
    numbers[index] = i
    index += 1

numbers = tuple(numbers)
letters = tuple(letters)

print(letters, "\n",  numbers)