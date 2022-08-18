class Car:
    def set_name(self, the_model, the_color, the_year):
        print('Constructor, self =' + str(self) )
        self.model = the_model
        self.color = the_color
        self.year = the_year

tesla_car = Car('MODEL X', 'White', 2020)

print(tesla_car)
