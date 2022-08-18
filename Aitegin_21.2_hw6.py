def get_first_word(a = 'Hello World'):
    if not sentence.isdigit():
        first_word = sentence.split()[0]
        return first_word
    else:
        return False

sentence = input()

# print(get_first_word())

def find_average(*args):
    average = 0
    for i in args:
        average += i
    return average // len(args)

# print(find_average(3, 3, 5, 6))

def check_password(password):
    if len(password) >= 6 and not password.isdigit() and not password.isalpha():
        return True
    return False

# print(check_password('a2311'))





