GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']

GeekTech['address'] = 'Ибраимова, 103'
GeekTech['phone_number'] = '0507 052 018'
GeekTech['instagram'] = 'geektech__kg'
GeekTech['courses'] = 'Backend', 'Android', 'Frontend', 'UI/UX Design', 'Ios', 'Fullstack', 'Basic Programming', 'The basis of the work is on the computer', 'English Courses'

set(GeekTech['courses'])

for key,value  in GeekTech.items():
    print(f'{key} : {value}')