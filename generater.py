# st='aaadddfdwfhiofw'
# dic={}

# for i in st:
#     dic[i] =  dic.get(i,0)+1
# print(dic)



# import threading

# def task():
#     for i in range(5):
#         print(i)
#         print(threading.current_thread().name)

# t1 = threading.Thread(target=task, name="Thread-1")
# t2 = threading.Thread(target=task, name="Thread-2")

# t1.start()
# t2.start()

# t1.join()
# t2.join()





# st="   hef fds jfdsfui  fwsf"
# ls = st.split(" ")

# print(ls)
# lst  = []
# for i in ls:
#     lst.append(i[::-1])
# print(lst)
# print(lst[::-1])
# l= lst[::-1]
# s = "".join(l)
# print(s)

# num = 17

# if num > 1:
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")


# def prime(nums):
#     bol=[False]*(nums+1)

#     for i in range(2,nums+1):
#         if bol[i]==False:
#             for j in range(2,i):
#                 # print(j)
#                 if(i%j==0):
#                     bol[i]=True
#                     break;
#     return bol

# # print(prime(100))

# res = prime(100)

# for i in range(2,len(res)):
#     if res[i]==False:
#         print(i)


# numbers = [10,40,20,50,30]

# # first = second = float("-inf")
# first = second = int("-inf")

# print(first)
# print(second)

# for n in numbers:
#     if n > first:
#         second = first
#         first = n
#     elif first > n > second:
#         second = n

# print(second)

text = "I Love Python"

result = " ".join(text.split()[::-1])

print(result)