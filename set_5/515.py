import re
s = input()
print(re.sub("\\d", lambda m: m.group() * 2, s))