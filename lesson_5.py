numbers =[1, 2,3, 4, 5]

new = dict(name = 'samat', age = 20)
student = {
    'name' : 'Azamat',
    'age' : 19,
    'height': 1.77,
    'hobby': ['chess', 'soccer', 'boxing']
}

for key, value in student.items():
    print(f'{key}: {value}')
student['married'] = False
# deleted = student.pop('hobby')
print(student.keys())
print(student.items())
print(student['name'])
del student['hobby'][1]
student['hobby'].remove('boxing')
student['hobby'].append('boxing')
student['age'] = 20

print(student)
print(type(student))
# print(new)