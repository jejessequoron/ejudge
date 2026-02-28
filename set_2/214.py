n = int(input())
s = list(map(int, input().split()))
d = {}
for i in range(n):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
M = d[s[0]]
for k in d:
    if M < d[k]:
        M = d[k]
t = sorted(d)
for l in t:
    if d[l] == M:
        print(l)
        break