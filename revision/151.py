def reverseWords(s):
        lst = s.split(' ')
        lst2 = lst[::-1]
        lst3 = ' '.join(lst2)
        lst3 = lst3.strip()
        return lst3
print(reverseWords("  hello world  "))


# PENDING THIS TYPE QUETION 
print(reverseWords("  hello     world  "))   # hello world