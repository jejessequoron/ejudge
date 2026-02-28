import re
s = input()
x = re.compile("^\\d+$")
print("Match" if x.match(s) else "No match")