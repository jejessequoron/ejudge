n = int(input())
l = []
d = {}
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
        d[s] = i + 1
for k in sorted(d):
    print(k, d[k])