class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def car_details(self):
        print("all the car details here : ",{self.brand} ,{self.model})
        return f"{self.brand}"
    

class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def electric_details(self):
        print("all the battery details here : ",{self.brand} ,{self.model})
        return f"hii dost"
    

my_tesla = ElectricCar("tesla","model","85kwh")
print(my_tesla.model)
print(my_tesla.full_name())
print(my_tesla.car_details())
print(my_tesla.electric_details())


# my_car = Car("Toyota","cololla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.car_details())