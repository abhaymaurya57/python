class Car:
    # constractor
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

    # method of class
    def display(self):
        print(self.name)
        print(self.brand)
        return f'name {self.name},brand {self.brand}'
    
# creating object of class
obj = Car('punch','tata')
print(obj.display())