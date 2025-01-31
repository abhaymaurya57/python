class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        # self.total_car
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.model}"
    def brand_name(self):
        return f"{self.__brand} + ! "
    def fuel(self):
        return "desil and petrol"
    
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel(self):
        return "electric charge"

my_tesla = ElectricCar("tesla","model","85kwh")
print(my_tesla.fuel())
Car("TATA","NANO")
print(safari.fuel())
print(safari.total_car)
print(Car.total_car)