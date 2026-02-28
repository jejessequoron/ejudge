import re
s = input()
p = input()
x = re.findall(re.escape(p), s)
print(len(x))