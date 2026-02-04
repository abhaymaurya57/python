char="aaabbbbcccrrr"
result={}
prev=""
count=0
# print(result["a"])

for i in char:
    if prev=="":
        prev=i
        count=1
    elif prev==i:
        count+=1
    else:
        result[prev]=count
        count=1
        prev=i
# store last character count
result[prev] = count    
print(result)

    