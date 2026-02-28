import re
s = input()
print("Yes" if re.match("^Hello", s) else "No")