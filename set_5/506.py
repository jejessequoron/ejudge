import re
s = input()
x = re.findall("\\S+@\\S+\\.\\S+", s)
if not x:
    print("No email")
else:
    print(x[0])