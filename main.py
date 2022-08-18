from time import sleep
i = 'a a a a a a a a a                a a a a a a a a a'
b = 'a               a                a                a'
g = 'a                aaaaaaaaaaaaaaaa                  aaaaaaaaaaaaaaaaaa'
d = g + 'aaaaaaaaaaaaaaaaaa'
c = 1

while 1 == 1:
    sleep(0.2)

    if c == 1 or c == 6:
        i = ' ' + i
        print(i)
    elif c == 3:
        print(g)
    else:
        print(b)
    c += 1
    if c > 6 :
        break

