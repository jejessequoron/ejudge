import re
s = input()
x = re.compile("\\b\\w+\\b")
print(len(x.findall(s)))