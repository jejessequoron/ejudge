import re
s = input()
x = re.match("Name: (.+), Age: (.+)", s)
print(x.group(1), x.group(2))