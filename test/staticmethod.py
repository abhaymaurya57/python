# ----------------------------------
#            introduction
# ----------------------------------

# class Cal:

#     def __init__(self,p):
#         self.p = p

#     def add(self,a,b):
#         return a+b+self.p
    
#     @staticmethod
#     def static(v,u):
#         return v+u
    
# obj = Cal(10)
# print(obj.add(4,3))

# print(Cal.static(3,4))


# --------------------------------------------
#                 gmail check
# --------------------------------------------


class Valid:

    def check(email):
        for i in email:
            if i=='@':
                return True
        return False

    @staticmethod
    def validattion(email):
        print('email is :',email)
        res = Valid.check(email)
        print("check email : ",res)
        if res:
            print("email is correct")
        else:
            print("Wrong email")  

obj = Valid()
Valid.validattion('abhmryagmail.com')