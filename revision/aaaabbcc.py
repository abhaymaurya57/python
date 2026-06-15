st = 'aaaabbbcc'
# output : a4b3c2
dic={}
for i in st:
    dic[i] = dic.get(i,0)+1
print(dic)