n = int(input())
s = list(map(int, input().split()))
M = max(s)
m = min(s)
for i in s:
    if (i == M):
        print(m, end=' ')
    else:
        print(i, end=' ')