cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[2])
print(len(cars))
for x in cars:
    print(x)

cars.append("honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("honda")
print(cars)