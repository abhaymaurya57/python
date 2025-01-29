import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))


#   create date objects 
x = datetime.datetime(2025,1,29)
print(x)

######     display the name of month ---
import datetime
x = datetime.datetime(2028,6,3)
print(x.strftime("%b,%p,%A"))
