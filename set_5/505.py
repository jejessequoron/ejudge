import re
s = input()
print("Yes" if re.search("^[A-Z]|[a-z].*\\d$", s) else "No")