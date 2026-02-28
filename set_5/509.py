import re
s = input()
x = re.findall("\\b\\w{3}\\b", s)
print(len(x))