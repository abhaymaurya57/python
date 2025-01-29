#A variable is only available from inside the region it is created. This is called scope.
def myfunc():
  x = 300
  print(x)

myfunc()
#*********************************
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#        global scope
x = 100

def myfunc():
  print(x)

myfunc()
print(x)

#---------naming variable-----
x = 400
def myfunc():
  x = 500
  print(x)
myfunc()
print(x)

#-------------groble keyword---------
def myfunc():
  global x
  x = 600

myfunc()

print(x)
#-------------------------
x = 700

def myfunc():
  global x
  x = 800
  print(x)

myfunc()

print(x)

#---------  nonlocal keyword  ------
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
    return x
  myfunc2()
  return x
print(myfunc1())