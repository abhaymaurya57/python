phone_no={
    'ram':12345,      
    'shyam':234567,
    'mohan':35678,
    }
print(phone_no)
print(phone_no['shyam'])

phone_no={
    'ram':12345,      #readable
    'shyam':234567,
    'mohan':35678,
    'ram':66666
    }
print(phone_no)

phone_no=dict([(
    'ram',12345),      
    ('shyam',234567),
    ('mohan',35678),
    ])
print(phone_no)
phone_no['madhav']={1111,2222,3333}
phone_no['shyam']={'shyam_home':5555,'shyam_work':4444}
print(phone_no['shyam']['shyam_work'])
print(phone_no.get('ram'))

data={
    1:'jenny',   #0 is not index
    2:'ram',
    0:'mohan'
}
print(data[0]) 

phone_no={
    'ram':12345,
    'shyam':234567,
    'mohan':35678,
    'rohit':3414124,
    'mohit':64363
    }
print(phone_no)
phone_no.pop('shyam')
print(phone_no)
del phone_no['ram']
print(phone_no)
print(phone_no.pop('mohan'))
print(phone_no)

phone_no={
    'ram':12345,
    'shyam':234567,
    'mohan':35678,
    'rohit':3414124,
    'mohit':64363
    }
print(phone_no)
print(phone_no.popitem())

phone_no={
    'ram':12345,
    'shyam':234567,
    'mohan':35678,
    'rohit':3414124,
    'mohit':64363
    }
print(phone_no.clear())
print(phone_no)

phone_no={
    'ram':12345,
    'shyam':234567,
    'mohan':35678,
    'rohit':3414124,
    'mohit':64363
    }
for i in phone_no:
    print(i)
    print(phone_no[i])
for i in phone_no.items():
    print(i)
print(phone_no)
phone_no2=phone_no.copy()
print(phone_no2)
print(len(phone_no))