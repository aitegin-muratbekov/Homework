
from random import choise

students = [i for i in range(1,19)]
print(students)
students.remove(12)
students.remove(14)
students.remove(15)
students.remove(8)
students.remove(11)
students.remove(17)
print (students)

while len(students) != 0:
    id = choise(students)
    name = input(f'name {id})