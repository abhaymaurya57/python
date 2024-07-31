def add(*numbers): #(4,5,3,6,8,6,7)
    c=0
    print(numbers[0])
    #numbers[0]= 4    tupels not change value
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
add(1,2)
add(6,5,4)
add(4,3,5,3,5,3,5,3)

#----** kwers--------
def add(*numbers,name):
    c=0
    print(numbers)
    print(name)
add(1,2,name="abhay")

# ---------------------

def add(*numbers):
    print(numbers)
add(1,2,"abhay")

#---------

def info_person(*args,**kwargs):

    for key,value in kwargs.items():
        print(key,value)

info_person(name="ram",age=30,dept="cse")
info_person(name="shyam",dept="cse")
