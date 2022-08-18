class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        if value < 0 or value.isalpha():
            raise AttributeError('Wrong value for age attibute it must be positive number')
        else:
            self.__cpu = value
    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
            self.__memory = value

    def make_computations(self):
        return self.__memory * 2
    #cpu это же строчный тип поэтому я не сделал с ним никаких арифметических операций

    def __gt__(self, other):
        return self.__memory > other.__memory
    def __lt__(self, other):
        return self.__memory < other.__memory
    def __eq__(self, other):
        return self.__memory == other.__memory

    def __str__(self):
        return f'Процессор {self.__cpu} Память {self.__memory}'


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_cards_number, call_to_number):
        if sim_cards_number -1 <= len(self.__sim_cards_list):
            return f'Идет звонок на номер {call_to_number} с сим карты {sim_cards_number} {self.__sim_cards_list[sim_cards_number-1]}'
    def __str__(self):
        return f'Phone симки {self.__sim_cards_list}'


class SmartPhone(Phone, Computer):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return f'проложен маршрут до {location}'
    def __str__(self):
        return f'Телефон Процессор {self.cpu} Память {self.memory}, симки{self.sim_cards_list}'



computer1 = Computer('i-3', 2)
phone_1 = Phone(['Beline', 'O'])
phone2 = SmartPhone('radeon', 4, ['Beline', 'O', 'Megacom'])
samsung = SmartPhone('Exinos', 8, ['Beline', 'O', 'Megacom'])
print(computer1, phone2, phone_1, samsung, sep = '\n')
print(computer1 > phone2, samsung < phone2, samsung == computer1 )
print(phone_1.call(1, 9965554445533))
print(samsung.use_gps('Бишкек'))
print(computer1.make_computations())