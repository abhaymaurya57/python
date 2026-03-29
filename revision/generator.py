# def myfun():
#     yield 1
#     yield 2
#     yield 3

# print(myfun())
# print(myfun())

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)