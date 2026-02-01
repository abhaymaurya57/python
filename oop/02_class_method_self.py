class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def name(self):
        print(f"what your name bro: {self.brand}")
        print("iner of name and call methos of full name:" ,my_car.full_name())

my_car = Car("Toyota","cololla")
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())
print(my_car.__dict__)
print(my_car.full_name())
my_car.name()