import re
s = input()
for c in re.findall("\\d", s):
    print(c, end=" ")