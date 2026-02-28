import re
s = input()
x = re.findall("\\d\\d+", s)
print(" ".join(x))