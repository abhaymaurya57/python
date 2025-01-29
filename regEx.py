import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("india", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "---", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())