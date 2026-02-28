import re
s = input()
x = re.findall("\\d\\d/\\d\\d/\\d\\d\\d\\d", s)
print(len(x))