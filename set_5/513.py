import re
s = input()
x = re.findall("\\w+", s)
print(len(x))