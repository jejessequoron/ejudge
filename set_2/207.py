n = int(input())
s = list(map(int, input().split()))
M = s[0]
k = 0
for i in range(1, n):
    if (M < s[i]):
        M = s[i]
        k = i
print(k + 1)