class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

my_tesla = ElectricCar("tesla","model","85kwh")
print(my_tesla.model)
print(my_tesla.full_name())


# my_car = Car("Toyota","cololla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())