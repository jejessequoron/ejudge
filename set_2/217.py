n = int(input())
d = {}
m = 0
for i in range(n):
    t = input()
    if t in d:
        d[t] += 1
    else:
        d[t] = 1
for k in d.keys():
    if d[k] == 3:
        m += 1
print(m)