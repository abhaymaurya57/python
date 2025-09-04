# zip() = groups values together element-wise.

# *zip() = splits them back ("unzips").

b={'a','b','c','d','e'}
c={1,2,3,4,5,6}
d=set(zip(b,c))
print(d)  #{('d', 4), ('a', 1), ('e', 5), ('b', 3), ('c', 2)}
letter,number=zip(*d)
print(letter)
print(number)

#**********************

names = ["Abhay", "Ravi", "Neha"]
scores = [85, 92, 78]

#***********************

for name, score in zip(names, scores):
    print(name, "scored", score)

#*********************

pairs = list(zip(range(10), range(1, 11)))
print(pairs)
