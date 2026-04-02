class Desktop:
    def __init__(self):
        self.__maxprice =25000

    def sell(self):
        return f"selling price: {self.__maxprice}"
    
    def set_max_price(self,price):
        if price>self.__maxprice:
            self.__maxprice =price

#object
DesktopObj = Desktop()
print(DesktopObj.sell())

DesktopObj.set_max_price(1250000)
print(DesktopObj.sell())