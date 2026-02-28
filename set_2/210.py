n = int(input())
s = list(map(int, input().split()))
l = sorted(s)
for i in range(n - 1, -1, -1):
    print(l[i], end=' ')