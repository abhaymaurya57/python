class Car:
    total_car = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        # self.total_car
        Car.total_car +=1

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def brand_name(self):
        return f"{self.__brand} + ! "
    def fuel(self):
        return "desil and petrol"
    
    @staticmethod
    def general_description():
         return "cars are means of transport"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

    def fuel(self):
        return "electric charge"

my_tesla = ElectricCar("tesla","model","85kwh")
print(my_tesla.fuel())
safari = Car("TATA","NANO")
# safari.model = "city"

print(safari.model)
# print(safari.fuel())
# print(safari.total_car)
# print(Car.total_car)
# print(safari.general_description())
# print(Car.general_description()) 