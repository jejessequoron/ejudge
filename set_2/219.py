n = int(input())
d = {}
for i in range(n):
    s, m = input().split()
    m = int(m)
    if s in d:
        d[s] += m
    else:
        d[s] = m
for k in sorted(d):
    print(k, d[k])