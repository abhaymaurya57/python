heights = input("Enter all heights separated by a space:")
# 151 153 140 160 167
heights_list=heights.split()
count = 0
for height in heights_list:
     count = count+1 
print(count)
for i in range(0,count): # 0 1 2 3 4 
    heights_list[i]=int(heights_list[i])
print(heights_list) 

total = 0
for person in heights_list:
     total += person
print(total)
avg = total/count
print("average height is :",round(avg))