class Person:
    def __init__(self,  fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'{self.fullname} {self.age} {self.is_married}'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def average(self):
        sum = 0
        for i in self.marks.values():
            sum += i
        return sum / len(self.marks.values())

class Teacher(Person):
    _salary = 1500
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience
    def count_salary(self):
        if self.experience > 3:
            self._salary = self._salary *3 + (self.experience-3)*(self._salary + self._salary/100*5)
        else:
            self._salary *= self.experience
        return self._salary

students = []
marlen = Person("Ormonbaev", 15, True)
teacher = Teacher('Natasha', 73, False, 5)

print(f'{teacher.introduce_myself()} {teacher.experience} {teacher.count_salary()}')

def create_students():
    aibek = Student('Korozbekov', 17, False,{'math' : 5,'physics' : 4, 'painting' : 3 })
    aitegin = Student('Rozbekov', 17, False,{'math' : 5,'physics' : 2, 'painting' : 3 })
    joma = Student('Orozbekov', 17, False,{'math' : 5,'physics' : 5, 'painting' : 4 })

    students.append(aibek)
    students.append(aitegin)
    students.append(joma)
    return students

create_students()


for self in students:
    print(f'{self.introduce_myself()} {str(self.marks)} {self.average()}')






