# class Database:

#     instance = None


#     def __new__(cls):
#         if cls.instance is None:
#             print("Creating object...")
#             cls.instance=super().__new__(cls)
#             print("one time only run....")
#         return cls.instance
    
#     def __init__(self):
#         print("Init called")

# t1 = Database()
# t2 = Database()
# t3 = Database()
# print(t1)
# print(t2)
# print(t3)
# print(t1 is t2 is t3)
# print(t1.instance)
# print(t2.instance)
# print(t3.instance)

# ------------------------------

class Singleton_Name:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Singleton created.....")
            cls._instance = super().__new__(cls)
            print("Only one time created")
        return cls._instance

    # def __init__(self, name):
    #     self.name = name       # bar bar name override kar de raha 

    def __init__(self, name):
        if not self._initialized:
            print("Init Called")
            self.name = name
            self._initialized = True
            print(self.__dict__)

obj1 = Singleton_Name("Abhay")
obj2 = Singleton_Name("Rahul")

print(obj1 is obj2)      # True
print(obj1.name)          # Rahul
print(obj2.name)          # Rahul

