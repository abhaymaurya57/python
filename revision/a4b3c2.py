# input: a4b3c2
# output: aaaabbbcc
st = "a4b3c2"
res=""
prev=""
for i in st:
    if i.isalpha():
        prev=i
    if i.isdigit():
        # print(i)
        res+=int(i)*prev
        prev=""
print(res)

# import re

# st = "a4b3c2"
# # Find all pairs of (letter, numbers)
# pairs = re.findall(r'([a-zA-Z])(\d+)', st)
# print(pairs)
# # Multiply the letter by the integer value of the number
# res = "".join(letter * int(number) for letter, number in pairs)

# print(res)  # Output: aaaabbbcc