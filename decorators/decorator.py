''' A Decorator in Python is a function that receives another function as argument.
The argument function is the one to be decorated by decorator.
The behaviour of argument function is extended by the decorator without actually modifying it. '''
import timeit
# Example 1:
def my_function(x):
   print("The number is=",x)
def my_decorator(some_function,num):
   def wrapper(num):
      print("Inside wrapper to check odd/even")
      if num%2 == 0:
         ret= "Even"
      else:
         ret= "Odd!"
      some_function(num)
      return ret
   print ("wrapper function is called")
   return wrapper
no=10
my_function = my_decorator(my_function, no)
print ("It is ",my_function(no))

# timeit with lambda
execution_time = timeit.timeit(lambda: my_function, number=1)
print("Execution time:", execution_time)


# exampl- 2

def my_decorator(some_function):
   def wrapper(num):
      print("Inside wrapper to check odd/even")
      if num%2 == 0:
         ret= "Even"
      else:
         ret= "Odd!"
      some_function(num)
      return ret
   print ("wrapper function is called")
   return wrapper

@my_decorator
def my_function(x):
   print("The number is=",x)
no=10
print ("It is ",my_function(no))