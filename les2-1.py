class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, new_value):
        self.__name = new_value

    def set_age(self, new_value):
        if new_value <= 0:
            raise AttributeError('Wrong value for age atribute it must be position')
        else:
            self.__age = new_value

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

    def info(self):
        return f'Name : {self.__name} Age: {self.__age}'

some_animal = Animal('dasha', 13)
some_animal.set_age(2)
print(some_animal.info())



