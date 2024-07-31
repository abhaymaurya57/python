#positianol Argument
def greet(name,dept):
    print(f"hii {name}")
    print(f"are you from {dept} department?")
greet("Abhay","cs")

#keyword argument

def greet(name,dept):
    print(f"hii {name}")
    print(f"are you from {dept} department?")
greet(dept="cs",name="Abhay")

#default argu...

def gree_t(name,age,dept="cs"):
    print( f"hii {name}")
    print(f"my age is {age}")
    print(f"are you from {dept} department?")
gree_t("Abhay",20) 

#arbitory/variaval lenght
def add(a,b):
    c=a+b
    print(f"sum is {c}")
add(3,5)

def add(*numbers): #(46,2)
    c=0
    for i in numbers:
        c=c+i
    print(f"sum is {c}")
add(3,5,6)
add(5,3,6,3,6,8,9,6,6,4,4,5,6)
