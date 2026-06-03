from abc import ABC,abstractmethod

class Vehicle(ABC):

    def __init__(self,vehicle_number, brand):
        self.__vehicle_number = vehicle_number
        self.__brand = brand
    
    @abstractmethod
    def calculate_rent(self,days):
        pass

#Car Class
class Car(Vehicle):

    def __init__(self, vehicle_number, brand,rent_per_day):
        super().__init__(vehicle_number, brand)
        self.__rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return days*self.__rent_per_day
    
#Bike Class
class Bike(Vehicle):

    def __init__(self,vehicle_number,brand,rent_per_day):
        super().__init__(vehicle_number,brand)
        self.__rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return days*self.__rent_per_day

# Objects
car = Car("UP15AB1234","Honda",1000)
bike = Bike("UP15XY5678","Hero",300)

Vehicle =[car,bike]

#polymorphism
for vehicle in Vehicle:
    print(vehicle.calculate_rent(5))
