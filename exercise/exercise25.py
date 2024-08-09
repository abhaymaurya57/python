def name(first_name,last_name):
    first_name_title=first_name.title()
    secound_name_title=last_name.title()
    return ({first_name_title},{secound_name_title})

first_name=input("Enter your first'name':?")
last_name=input("Enter your last 'name':?")
result=name(first_name,last_name)
print(result)