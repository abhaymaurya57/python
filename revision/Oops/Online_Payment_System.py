from abc import ABC,abstractmethod

class Payment(ABC):

# Abstract Class
    @abstractmethod
    def pay(self,amount):
        pass

#Credit Card Payment
class CreditCardPayment(Payment):
    def __init__(self,card_number):
        self.__card_number = card_number  # Encapsulation

    def pay(self,amount):
        print(f"Credit Card Payment of ${amount} successful")
    
# UPI Payment

class UPIPayment(Payment):

    def __init__(self,upi_id):
        self.__upi_id = upi_id  # EncapSulation

    def pay(self,amount):
        print(f"UPI Payment of ${amount} successful")
    
# Net Banking Payment
class NetBankingPayment(Payment):
    
    def __init__(self,bank_name):
        self.__bank_name = bank_name  # Encapsulation

    def pay(self,amount):
        print(f"Net Banking Payment of ${amount} successful")

#Main
p1=CreditCardPayment("1234-5678-9012")
p2 =UPIPayment("abhay@upi")
p3 = NetBankingPayment("SBI")

Payments=[p1,p2,p3]

for payment in Payments:
    if isinstance(payment,CreditCardPayment):
        payment.pay(5000)
    elif isinstance(payment,UPIPayment):
        payment.pay(3000)
    else:
        payment.pay(7000)